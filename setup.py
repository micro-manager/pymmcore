# Setup for pymmcore
#
# Copyright (C) 2020-2021 Board of Regents of the University of Wisconsin
#                         System
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License, version 2.1, as published
# by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Author: Mark A. Tsuchida

from contextlib import contextmanager, nullcontext
import os
import os.path
import platform
from pathlib import Path
from typing import TYPE_CHECKING

import numpy
import setuptools.command.build_ext
import setuptools.command.build_py
from setuptools import Extension, setup

if TYPE_CHECKING:
    from typing import ContextManager, Iterable

PKG_NAME = "pymmcore"
SWIG_MOD_NAME = "pymmcore_swig"
IS_WINDOWS = platform.system() == "Windows"
ROOT = Path(__file__).parent
MMCorePath = ROOT / "mmCoreAndDevices" / "MMCore"
MMDevicePath = ROOT / "mmCoreAndDevices" / "MMDevice"

# We build MMCore from sources, into the Python extension. MMCore depends on
# MMDevice. However, we need to build MMDevice separately from MMCore, because
# it requires different preprocessor macros to be defined. For this purpose, we
# make use of a rather obscure feature of distutils/setuptools called
# build_clib. There may be other ways to do this....


# Customize 'build_py' to run 'build_ext' first; otherwise the SWIG-generated
# .py file gets missed.
class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command("build_ext")
        super().run()


# Customize 'build_ext' to trigger 'build_clib' first.
class build_ext(setuptools.command.build_ext.build_ext):
    def run(self):
        self.run_command("build_clib")
        super().run()


define_macros = [("MMDEVICE_CLIENT_BUILD", None)]
if IS_WINDOWS:
    define_macros += [("NOMINMAX", None), ("_CRT_SECURE_NO_WARNINGS", None)]


mmdevice_build_info = {
    "sources": [str(x.relative_to(ROOT)) for x in MMDevicePath.glob("*.cpp")],
    "include_dirs": ["mmCoreAndDevices/MMDevice"],
    "macros": define_macros,
}

omit = ["unittest"] + (["Unix"] if IS_WINDOWS else ["Windows"])
mmcore_sources = [
    str(x.relative_to(ROOT))
    for x in MMCorePath.rglob("*.cpp")
    if all(o not in str(x) for o in omit)
]

mmcore_libraries = ["MMDevice"]
if not IS_WINDOWS:
    mmcore_libraries.extend(["dl"])

if not IS_WINDOWS:
    cflags = [
        "-std=c++14",
        "-fvisibility=hidden",
        "-Wno-deprecated",  # Hide warnings for throw() specififiers
        "-Wno-unused-variable",  # Hide warnings for SWIG-generated code
    ]
    if "CFLAGS" in os.environ:
        cflags.append(os.environ["CFLAGS"])
    os.environ["CFLAGS"] = " ".join(cflags)

swig_opts = [
    "-c++",
    "-python",
    "-builtin",
    "-I./mmCoreAndDevices/MMDevice",
    "-I./mmCoreAndDevices/MMCore",
]


mmcore_extension = Extension(
    f"{PKG_NAME}._{SWIG_MOD_NAME}",
    sources=mmcore_sources
    + [
        os.path.join(
            "src",
            PKG_NAME,
            f"{SWIG_MOD_NAME}.i",
        )
    ],
    swig_opts=swig_opts,
    include_dirs=[
        numpy.get_include(),
        "./mmCoreAndDevices/MMDevice",
        "./mmCoreAndDevices/MMCore",
    ],
    libraries=mmcore_libraries,
    define_macros=define_macros,
)


@contextmanager
def add_virtual(method_names: Iterable[str]):
    """Context in which the specified methods are declared virtual in MMCore.h."""
    MMCoreh = MMCorePath / "MMCore.h"
    original_text = MMCoreh.read_text()
    modified = False
    new_lines = []
    for line in original_text.splitlines():
        if any(x + "(" in line for x in method_names):
            line = "   virtual " + line.lstrip()
            modified = True
        new_lines.append(line)
    if modified:
        MMCoreh.write_text("\n".join(new_lines))
    try:
        yield
    finally:
        if modified:
            MMCoreh.write_text(original_text)


# Check if POLYMORPHIC_CMMCORE is set in the environment variables
# this enables the director feature on the MMCore class
POLYMORPHIC = os.getenv("POLYMORPHIC_CMMCORE", "").lower() in ("true", "1", "yes")
if POLYMORPHIC:
    swig_opts.append("-DPOLYMORPHIC_CMMCORE")
    virtual_methods = ["setFocusDevice"]
    modified_headers: ContextManager = add_virtual(virtual_methods)
else:
    modified_headers = nullcontext()


with modified_headers:
    setup(
        ext_modules=[mmcore_extension],
        libraries=[("MMDevice", mmdevice_build_info)],
        cmdclass={"build_ext": build_ext, "build_py": build_py},
    )

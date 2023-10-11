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

import os
import os.path
import platform
from pathlib import Path

import numpy
import setuptools.command.build_ext
import setuptools.command.build_py
from setuptools import Extension, setup

PKG_NAME = "pymmcore"
SWIG_MOD_NAME = "pymmcore_swig"
IS_WINDOWS = platform.system() == "Windows"
IS_MACOS = platform.system() == "Darwin"
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


mmdevice_build_info = {
    "sources": [str(x.relative_to(ROOT)) for x in MMDevicePath.glob("*.cpp")],
    "include_dirs": ["mmCoreAndDevices/MMDevice"],
    "macros": [("MODULE_EXPORTS", None)],
}

if IS_WINDOWS:
    define_macros = [
        ("_CRT_SECURE_NO_WARNINGS", None),
        # These would not be necessary if _WIN32 or _MSC_VER were used correctly.
        ("WIN32", None),
        ("_WINDOWS", None),
        # See DeviceUtils.h
        ("MMDEVICE_NO_GETTIMEOFDAY", None),
    ]
    mmdevice_build_info["macros"].extend(define_macros)
else:
    define_macros = []

omit = ["unittest"] + (["Unix"] if IS_WINDOWS else ["Windows"])
mmcore_sources = [
    str(x.relative_to(ROOT))
    for x in MMCorePath.rglob("*.cpp")
    if all(o not in str(x) for o in omit)
]

mmcore_libraries = ["MMDevice"]
if IS_WINDOWS:
    mmcore_libraries.extend(["Iphlpapi", "Advapi32"])
else:
    mmcore_libraries.extend(["dl"])

if not IS_WINDOWS:
    cflags = ["-std=c++14"]
    if "CFLAGS" in os.environ:
        cflags.insert(0, os.environ["CFLAGS"])
    os.environ["CFLAGS"] = " ".join(cflags)


# MMCore on macOS currently requires these frameworks (for a feature that
# should be deprecated). Frameworks need to appear on the linker command line
# before the object files, so extra_link_args doesn't work.
if IS_MACOS:
    ldflags = ["-framework", "CoreFoundation", "-framework", "IOKit"]
    if "LDFLAGS" in os.environ:
        ldflags.insert(0, os.environ["LDFLAGS"])
    os.environ["LDFLAGS"] = " ".join(ldflags)


mmcore_extension = Extension(
    f"{PKG_NAME}._{SWIG_MOD_NAME}",
    sources=mmcore_sources + [os.path.join(PKG_NAME, f"{SWIG_MOD_NAME}.i")],
    swig_opts=[
        "-c++",
        "-py3",
        "-builtin",
        "-I./mmCoreAndDevices/MMDevice",
        "-I./mmCoreAndDevices/MMCore",
    ],
    include_dirs=[numpy.get_include()],
    libraries=mmcore_libraries,
    define_macros=define_macros,
)

setup(
    ext_modules=[mmcore_extension],
    libraries=[("MMDevice", mmdevice_build_info)],
    cmdclass={"build_ext": build_ext, "build_py": build_py},
)

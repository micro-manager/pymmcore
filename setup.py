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

import distutils.file_util
import distutils.util
import glob
import numpy
import os
import os.path
import setuptools
import setuptools.command.build_ext
import setuptools.command.build_py

pkg_name = 'pymmcore'
swig_mod_name = 'pymmcore_swig'
ext_mod_name = '.'.join((pkg_name, '_' + swig_mod_name))


# We build MMCore from sources, into the Python extension. MMCore depends on
# MMDevice. However, we need to build MMDevice separately from MMCore, because
# it requires different preprocessor macros to be defined. For this purpose, we
# make use of a rather obscure feature of distutils/setuptools called
# build_clib. There may be other ways to do this....


# Customize 'build_py' to run 'build_ext' first; otherwise the SWIG-generated
# .py file gets missed.
class build_py(setuptools.command.build_py.build_py):
    def run(self):
        self.run_command('build_ext')
        super().run()


# Customize 'build_ext' to trigger 'build_clib' first.
class build_ext(setuptools.command.build_ext.build_ext):
    def run(self):
        self.run_command('build_clib')
        super().run()


is_windows = distutils.util.get_platform().startswith('win')
is_macos = distutils.util.get_platform().startswith('macosx')

windows_defines = [
    ('_CRT_SECURE_NO_WARNINGS', None),

    # These would not be necessary if _WIN32 or _MSC_VER were used correctly.
    ('WIN32', None),
    ('_WINDOWS', None),

    # See DeviceUtils.h
    ('MMDEVICE_NO_GETTIMEOFDAY', None),
]


mmdevice_build_info = {
    'sources': glob.glob('mmCoreAndDevices/MMDevice/*.cpp'),
    'include_dirs': [
        'mmCoreAndDevices/MMDevice',
    ],
    'macros': [
        ('MODULE_EXPORTS', None),
    ],
}

if is_windows:
    mmdevice_build_info['macros'].extend(windows_defines)


mmcore_source_globs = [
    'mmCoreAndDevices/MMCore/*.cpp',
    'mmCoreAndDevices/MMCore/Devices/*.cpp',
    'mmCoreAndDevices/MMCore/LibraryInfo/*.cpp',
    'mmCoreAndDevices/MMCore/LoadableModules/*.cpp',
    'mmCoreAndDevices/MMCore/Logging/*.cpp',
]

mmcore_sources = []
for g in mmcore_source_globs:
    mmcore_sources += glob.glob(g)
if is_windows:
    mmcore_sources = [f for f in mmcore_sources if 'Unix' not in f]
else:
    mmcore_sources = [f for f in mmcore_sources if 'Windows' not in f]


mmcore_libraries = [
    'MMDevice',
]
if is_windows:
    mmcore_libraries.extend([
        'Iphlpapi',
        'Advapi32',
    ])
else:
    mmcore_libraries.extend([
        'dl',
    ])


if not is_windows:
    cflags = [
        '-std=c++14',
    ]
    if 'CFLAGS' in os.environ:
        cflags.insert(0, os.environ['CFLAGS'])
    os.environ['CFLAGS'] = ' '.join(cflags)


# MMCore on macOS currently requires these frameworks (for a feature that
# should be deprecated). Frameworks need to appear on the linker command line
# before the object files, so extra_link_args doesn't work.
if is_macos:
    ldflags = [
        '-framework', 'CoreFoundation',
        '-framework', 'IOKit',
    ]
    if 'LDFLAGS' in os.environ:
        ldflags.insert(0, os.environ['LDFLAGS'])
    os.environ['LDFLAGS'] = ' '.join(ldflags)


mmcore_defines = []
if is_windows:
    mmcore_defines.extend(windows_defines)


mmcore_extension = setuptools.Extension(
    ext_mod_name,
    sources=mmcore_sources + [
        os.path.join(pkg_name, swig_mod_name + '.i'),
    ],
    swig_opts=[
        '-c++',
        '-py3',
        '-builtin',
        '-I./mmCoreAndDevices/MMDevice',
        '-I./mmCoreAndDevices/MMCore',
    ],
    include_dirs=[
        numpy.get_include(),
    ],
    libraries=mmcore_libraries,
    define_macros=mmcore_defines,
)


# See maintainer notes!
python_req = '>=3.6'
numpy_req = '>=1.12.0'


setuptools.setup(
    packages=setuptools.find_packages(include=(pkg_name + '*',)),
    ext_modules=[mmcore_extension],
    libraries=[
        ('MMDevice', mmdevice_build_info),
    ],
    python_requires=python_req,
    setup_requires=[
        'numpy' + numpy_req,
    ],
    install_requires=[
        'numpy' + numpy_req,
    ],
    cmdclass={
        'build_ext': build_ext,
        'build_py': build_py,
    },
    package_data={
        'pymmcore': ['*.pyi', 'py.typed'],
    },
)

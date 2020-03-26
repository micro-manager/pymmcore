# Setup for pymmcore
#
# Author: Mark Tsuchida
#
# Copyright (C) 2020 Board of Regents of the University of Wisconsin System
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

import distutils.command.build_ext
import distutils.file_util
import distutils.util
import glob
import numpy
import os
import setuptools

py_mod_name = 'pymmcore'
ext_mod_name = '_' + py_mod_name


# We build MMCore from sources, into the Python extension. MMCore depends on
# MMDevice. However, we need to build MMDevice separately from MMCore, because
# it requires different preprocessor macros to be defined. For this purpose, we
# make use of a rather obscure feature of distutils/setuptools called
# build_clib. There may be other ways to do this....

# Customize build_ext to also run build_clib and also copy the Python module
class build_ext(distutils.command.build_ext.build_ext):
    def run(self):
        self.run_command('build_clib')
        distutils.command.build_ext.build_ext.run(self)
        distutils.file_util.copy_file(
            'micro-manager/MMCorePy_wrap/' + py_mod_name + '.py',
            py_mod_name + '.py')


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
    'sources': glob.glob('micro-manager/MMDevice/*.cpp'),
    'include_dirs': [
        'micro-manager/MMDevice',
    ],
    'macros': [
        ('MODULE_EXPORTS', None),
    ],
}

if is_windows:
    mmdevice_build_info['macros'].extend(windows_defines)


mmcore_source_globs = [
    'micro-manager/MMCore/*.cpp',
    'micro-manager/MMCore/Devices/*.cpp',
    'micro-manager/MMCore/LibraryInfo/*.cpp',
    'micro-manager/MMCore/LoadableModules/*.cpp',
    'micro-manager/MMCore/Logging/*.cpp',
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
    # On Windows, Boost headers automatically configure these
    mmcore_libraries.extend([
        'dl',
        'boost_date_time',
        'boost_system',
        'boost_thread',
    ])


# MMCore on macOS currently requires these frameworks (for a feature that
# should be deprecated). Frameworks need to appear on the linker command line
# before the object files, so extra_link_args doesn't work.
if is_macos:
    ldflags = [
        '-framework', 'CoreFoundation',
        '-framework', 'IOKit',
    ]
    if 'LDFLAGS' in os.environ:
        ldflags = [os.environ['LDFLAGS']] + ldflags
    os.environ['LDFLAGS'] = ' '.join(ldflags)


mmcore_defines = []
if is_windows:
    mmcore_defines.extend(windows_defines)


mmcore_extension = setuptools.Extension(
    ext_mod_name,
    sources=mmcore_sources + [
        'micro-manager/MMCorePy_wrap/MMCorePy.i',
    ],
    swig_opts=[
        '-c++',
        '-py3',
        '-builtin',
        '-module', py_mod_name,
        '-I./micro-manager/MMDevice',
        '-I./micro-manager/MMCore',
    ],
    include_dirs=[
        numpy.get_include(),
    ],
    libraries=mmcore_libraries,
    define_macros=mmcore_defines,
)


# See maintainer notes!
python_req = '>=3.5'
numpy_req = '>=1.10.4'


setuptools.setup(
    py_modules=[py_mod_name],
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
    },
)

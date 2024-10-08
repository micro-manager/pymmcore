# Copyright 2020-2024 Board of Regents of the University of Wisconsin System
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

project(
    'pymmcore',
    'cpp',
    version: '11.1.1.71.1.dev0',
    meson_version: '>=1.3.0',
    default_options: [
        'cpp_std=c++14',
        'warning_level=3',
    ],
    # Until MMDevice and MMCore are available individually, we need to use them
    # from the same git submodule, so this is a bit of a hack:
    subproject_dir: 'mmCoreAndDevices',
)

cxx = meson.get_compiler('cpp')
if cxx.get_id() in ['gcc', 'clang']
    add_project_arguments('-Wno-deprecated', language: 'cpp')        # throw()
    # Disable warnings triggered by SWIG-generated code:
    add_project_arguments('-Wno-unused-parameter', language: 'cpp')
    add_project_arguments('-Wno-unused-variable', language: 'cpp')
endif
if cxx.get_id() in ['msvc', 'clang-cl']
    add_project_arguments('-DNOMINMAX', language: 'cpp')
    add_project_arguments('-D_CRT_SECURE_NO_WARNINGS', language: 'cpp')
    # Disable warnings triggered by SWIG-generated code:
    add_project_arguments('/wd4100', language: 'cpp')
    add_project_arguments('/wd4101', language: 'cpp')
    add_project_arguments('/wd4127', language: 'cpp')
    add_project_arguments('/wd4456', language: 'cpp')
    add_project_arguments('/wd4706', language: 'cpp')
endif

fs = import('fs')

python = import('python').find_installation(pure: false)

threads_dep = dependency('threads')

numpy_abs_incdir = run_command(
    python, '-c', 'import numpy; print(numpy.get_include())',
    check: true,
).stdout().strip()
# The "correct" way would be to "detect" NumPy as a dependency. Since we are
# cutting corners, we need to use a relative path as if the NumPy headers are
# part of this project.
numpy_incdirs = include_directories(fs.relative_to(numpy_abs_incdir, '.'))

swig = find_program('swig', native: true)

# For now, use MMCore as a subproject. This may be changed to using as a
# proper dependency via a wrap, but that will likely require better SWIG
# support by Meson in order to get the SWIG include directories from the
# dependency object.
mmcore_proj = subproject(
    'MMCore',
    default_options: {
        'default_library': 'static',
        'tests': 'disabled',  # Avoid Catch2 subproject in sdist
    },
)
mmcore_dep = mmcore_proj.get_variable('mmcore')

swig_include_dirs = mmcore_proj.get_variable('swig_include_dirs')

subdir('src/pymmcore')

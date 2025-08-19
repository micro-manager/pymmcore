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
    version: '11.10.0.74.0',
    meson_version: '>=1.4.0',
    default_options: [
        'cpp_std=c++14',
        'warning_level=3',
    ],
)

cxx = meson.get_compiler('cpp')
if cxx.get_id() in ['gcc', 'clang']
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

numpy_dep = dependency('numpy')

swig = find_program('swig', native: true)

# For now, use MMCore as a subproject. This may be changed to using as a
# proper dependency via a wrap, but that will likely require better SWIG
# support by Meson in order to get the SWIG include directories from the
# dependency object.
mmcore_proj = subproject(
    'mmcore',
    default_options: {
        'default_library': 'static',
        'tests': 'disabled',  # Avoid Catch2 subproject in sdist
    },
)
mmcore_dep = mmcore_proj.get_variable('mmcore')

swig_include_dirs = mmcore_proj.get_variable('swig_include_dirs')

subdir('src/pymmcore')

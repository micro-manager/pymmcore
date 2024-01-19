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

swig_incdir_args = []
foreach abspath : swig_include_dirs
    # Use relative path for readability only.
    swig_incdir_args += '-I' + fs.relative_to(
        abspath,
        meson.project_build_root(),
    )
endforeach

swig_gen = custom_target(
    'swig-pymmcore',
    input: 'pymmcore_swig.i',
    output: [
        # Note: Order is significant and used below!
        'pymmcore_swig_wrap.cpp',  # @OUTPUT0@, swig_gen[0]
        'pymmcore_swig_wrap.h',    # @OUTPUT1@, swig_gen[1]
        'pymmcore_swig.py',
    ],
    depfile: 'pymmcore_swig_wrap.d',
    command: [
        swig,
        '-c++',
        '-python',  # -py3 removed in SWIG 4.1
        '-builtin',
        swig_incdir_args,
        '-MD', '-MF', '@DEPFILE@',
        '-o', '@OUTPUT0@',
        '-oh', '@OUTPUT1@',
        '-outdir', '@OUTDIR@',
        '@INPUT@',
    ],
    # Would be nice to install just the .py, but there seems to be no way to
    # split out a file from the target. So leave in the .h/.cpp.
    install: true,
    install_dir: python.get_install_dir() / 'pymmcore',
    install_tag: 'python-runtime',
)
swig_gen_cpp_sources = [swig_gen[0], swig_gen[1]]

python.extension_module(
    '_pymmcore_swig',
    swig_gen_cpp_sources,
    dependencies: [
        mmcore_dep,
        threads_dep,
    ],
    include_directories: [
        numpy_incdirs,
    ],
    install: true,
    subdir: 'pymmcore',
)

version_py = configure_file(
    configuration: {'VERSION': meson.project_version()},
    input: '_version.py.in',
    output: '_version.py',
    install: true,
    install_dir: python.get_install_dir() / 'pymmcore',
    install_tag: 'python-runtime',
)

pymmcore_sources = files(
    '__init__.py',
    '__init__.pyi',
    'py.typed',
)

python.install_sources(
    pymmcore_sources,
    subdir: 'pymmcore',
)

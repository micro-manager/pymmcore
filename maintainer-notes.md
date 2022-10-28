Versioning scheme
-----------------

Cf. PEP 440.

Concatenate the MMCore version, MMDevice device interface version, and an extra
pymmcore-specific suffix. For example, pymmcore 10.1.1.69.0 wraps MMCore 10.1.1
and works with device adapters built for device interface version 69. The
final suffix can be incremented to create a new release for improvements to the
pymmcore wrapper.

(Note that the device interface version can change without a change to the
MMCore version, although this is relatively uncommon. Also, we are leaving out
the module interface version, which rarely changes.)

The correspondence to MMCore and device interface versions is checked in the
smoke test.

Note that we can support multiple MMCore versions, possibly retroactively, by
maintaining separate branches; this can ease transition when the device
interface version changes. Such branches should be named `mmcore-x.y.z.w`.

When upgrading the MMCore version (by bumping the mmCoreAndDevices submodule
commit), the pymmcore version in `setup.cfg` should be updated together.


Release procedure
-----------------

Prepare two commits, one removing `.dev0` from the version and a subsequent one
bumping the patch version and re-adding `.dev0`. Tag the former with `v`
prefixed to the version:
```bash
git checkout main

vim pymmcore/_version.py  # Remove .dev0
git commit -a -m 'Version 1.2.3.42.4'
git tag -a v1.2.3.42.4 -m Release

vim pymmcore/_version.py  # Set version to 1.2.3.42.5.dev0
git commit -a -m 'Version back to dev'

git push origin v1.2.3.42.4
git push
```

This triggers a build, since our GitHub workflow builds on push, including when
it's an annotated tag. The build, when successful, automatically uploads to
PyPI when the tag name starts with `v`.

Pushing the tag also creates a GitHub release, which can be edited to add
binaries. Upload the Windows, macOS, and manylinux wheels and source
distribution as a backup and second source.


ABI Compatibility
-----------------

- The Python platform and ABI compatibility is all handled by the Wheel system.
  (But see below re MSVC versions.)

- NumPy ABI compatibility needs to be maintained by building against a
  reasonably old version of NumPy when packaging for public distribution (cf.
  https://github.com/numpy/numpy/issues/5888).

  In practice, we should use the oldest NumPy for which wheels are available on
  PyPI for the given Python version (and all 3 platforms):
  - Python 3.5 - NumPy 1.10.4
  - Python 3.6 - NumPy 1.12.0
  - Python 3.7 - NumPy 1.14.5
  - Python 3.8 - NumPy 1.17.3
  - Python 3.9 - NumPy 1.19.3
  - Python 3.10 - NumPy 1.21.3 (Windows: amd64 only)
  - Python 3.11 - NumPy 1.23.2


### Windows

- MSVC version. Python 3.5 and later are built with MSVC 14.x (i.e. Visual
  Studio 2015 to 2019). However, the official Python installer ships with its
  own copy of the VC runtime (in particular, `vcruntime140.dll`). This means
  that (in theory) our extension module must be built with an MSVC version that
  is not newer than the runtime shipped with Python. I say "in theory" because
  it is not clear if this actually results in problems, but let's play it safe.

  Python prints the MSVC version used to build itself when started. This
  version may change with the patch version of Python. Here are a few examples:
  - Python 3.5.4 (64-bit): MSC v.1900 = VS2015
  - Python 3.6.8 (64-bit): MSC v.1916 = VS2017
  - Python 3.7.6 (64-bit): MSC v.1916
  - Python 3.8.1 (64-bit): MSC v.1916
  - Python 3.9.1 (64-bit): MSC v.1927 = VS2019
  - Python 3.8.7 (64-bit): MSC v.1928 = VS2019
  - Python 3.10.0 (64-bit): MSC v.1929 = VS2019
  - Python 3.11.0 (64-bit): MSC v.1933 = VS2022

  In general, it is probably safest to always build with VS2015 (older patch
  versions of Python 3.7-3.8 may be built with VS2015). This can be done by
  running `setup.py` inside the VS2015 Native Tools Command Prompt (this works
  because we use `setuptools`; with `distutils` extra environment variables are
  needed).

  It should also be noted that some Python package wheels (e.g. SciPy) ship a
  copy of `msvcp140.dll` (the C++ runtime) and other "140" DLLs. If they are
  loaded first, the version is pinned.

  We might want to pay attention to all this if/when Micro-Manager starts
  shipping with device adapters built with newer MSVC versions in the future.

- Should we ship `msvcp140.dll` as part of the wheel? Given how the Python.org
  Windows installers are designed for non-admin installation, we technically
  should.


### macOS

- `MACOSX_DEPLOYMENT_TARGET` should be set to match the Python.org Python we
  are building for, as much as reasonably possible. Currently, `10.9` is the
  best value for Python 3.5-3.10.
- Python up to 3.7 also provide a `10.6`-compatible installer (which also
  includes 32-bit binaries). However, it is not feasible to set up a new build
  environment that can (correctly) build for `<10.9`.
- `10.9` is the oldest version that links with `libc++`; older deployment
  targets would link with `libstdc++`.
- Our extension will still work if our deployment target is newer than
  Python's, so long as it is not newer than the host macOS version.
- We can build `pymmcore` with `libc++` and it works fine with device adapters
  built with `libstdc++` (because the interface is POD-only).
- In the not-so-likely event that our extension uses symbols only available in
  macOS SDKs newer than the deployment target, those symbols will appear as
  'weak' in `nm -mu`.
  - Not all weak symbols are a problem. There will always be a few from the C++
    standard library that are harmless.
- The built extension should be checked for undefined symbols (`nm -mu`) that
  are "dynamically looked up", other than those starting with `_Py` or `__Py`.
  There should be none if the build is correct.


### Linux

- The manylinux docker images appear to solve all our problems.


Dependency and tool versions
----------------------------

- The Python and NumPy version requirements in `setup.py` should be set so that
  `pip` just works.
  - NumPy wheels for the Python-NumPy version combination should be available
    on PyPI (for mac/linux/windows) for the versions we support.
  - _We_ should provide wheels for all Python versions we claim to support,
    built agains the oldest NumPy version that we claim to support. Thus, any
    issue with the build or our CI will limit the lowest supported versions.
  - The required version ranges can be made platform-specific if necessary (see
    setuptools docs)

- Swig.
  - Swig 1.x generates code that is no longer compatible with Python 3.x.
  - Swig 4.x should be used.


Building with debug symbols on Windows
--------------------------------------

Since there is no easy way to pass compile and linker options to `build_clib`,
the easiest hack is to edit the local Python installation's
`Lib/distutils/_msvccompiler.py` to add the compiler flag `/Zi` and linker flag
`/DEBUG:FULL` (see the method `initialize`). This produces `vc140.pdb`.

(The "normal" method would be to run `setup.py build_clib` and `setup.py
build_ext` with the `--debug` option, and run with `python_d.exe`. But then we
would need a debug build of NumPy, which is hard to build on Windows.)


Resources
---------

- [Windows Compilers](https://wiki.python.org/moin/WindowsCompilers) on Python Wiki
- [MacPython: Spinning wheels](https://github.com/MacPython/wiki/wiki/Spinning-wheels) (macOS ABI)
- [manylinux](https://github.com/pypa/manylinux) Docker images; [PEP
  513](https://python.org/dev/peps/pep-0513),
  [571](https://python.org/dev/peps/pep-0571), and
  [599](https://python.org/dev/peps/pep-0599)

- Windows [DLL search order](https://docs.microsoft.com/en-us/windows/win32/dlls/dynamic-link-library-search-order)
- Unmaintained Apple [tech
  note](https://developer.apple.com/library/archive/technotes/tn2064/_index.html)
  describing `MACOSX_DEPLOYMENT_TARGET`

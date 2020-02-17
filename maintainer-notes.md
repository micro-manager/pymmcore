TODOs
-----

- Determine versioning scheme. In terms of API, the MMCore version (which
  follows Semantic Versioning) is good, although pymmcore may add a few
  functions that are not in MMCore. For this reason we should probably add a
  suffix to the MMCore version. We should make sure to conform to **PEP 440**.
  Note that the device interface version should _not_ be used, because that is
  not what projects depending on pymmcore should care about in their
  `requirements.txt`.


Maintainer Notes
----------------

- The Python platform and ABI compatibility is all handled by the Wheel system.

- NumPy ABI compatibility needs to be maintained by building against a
  reasonably old version of NumPy when packaging for public distribution (cf.
  https://github.com/numpy/numpy/issues/5888).

- MSVC version. Python 3.5-3.8 are built with MSVC 14.x (i.e. Visual Studio
  2015 to 2019). _However,_ the official Python installer ships with its own
  copy of the VC runtime. This means that our extension module must be built
  with an MSVC version that is not newer than the runtime shipped with Python.
  Getting this wrong results in crashes that are very confusing to diagnose.

  Python prints the MSVC version used to build itself when started:
  - Python 3.5.4 (64-bit): MSC v.1900 = VS2015 (14.0)
  - Python 3.6.8 (64-bit): MSC v.1916 = VS2017 (14.1)
  - Python 3.7.6 (64-bit): MSC v.1916
  - Python 3.8.1 (64-bit): MSC v.1916

  In general, it is probably safest to **always build with VS2015** (older
  minor versions of Python `>=3.6` may be built with VS2015). This can be done
  by running `setup.py` inside the VS2015 Native Tools Command Prompt (this
  works because we use `setuptools`; with `distutils` extra environment
  variables are needed).

  It should also be noted that some Python package wheels (e.g. SciPy) ship a
  copy of `msvcp140.dll` (the C++ runtime) and other "140" DLLs. If they are
  loaded first, the version is fixed.

  If/when Micro-Manager starts shipping with device adapters built with newer
  MSVC versions **in the future, this is going to become a problem**.

  One workaround will be to have the user delete all copies of the VC runtime
  within the Python installation, so that the system copy is used. But we would
  like to avoid this except perhaps as a way to diagnose issues. It is fragile
  because a subsequent package installation via `pip` could introduce an older
  copy.

- Should we ship `msvcp140.dll` as part of the wheel? Perhaps technically we
  should.

- The Python and NumPy version requirements in `setup.py` should be set so that
  `pip` just works.
  - NumPy wheels for the Python-NumPy version combination should be available
    on PyPI (for mac/linux/windows) for the versions we support.
  - _We_ should provide wheels for all Python versions we claim to support,
    built agains the oldest NumPy version that we claim to support. Thus, any
    issue with the build or our CI will limit the lowest supported versions.
  - The required version ranges can be made platform-specific if necessary (see
    setuptools docs)

- Boost should linked as a static library (for distribution).
  - Currently, MMCore depends on Boost.System, Boost.Datetime, and Boost.Thread
    (and other header-only libraries).
  - `setup.py` expects Boost to be taken care of externally.
  - We need to choose a version of Boost that is (1) new enough to build with
    the compiler required by the target Python version and (2) old enough for
    MMCore to build. Probably (1) is a more stringent requirement.
  - Local or user builds can of course just use the Boost shared libraries on
    their system, if compatible.
  - Future versions of MMCore (once Visual Studio 2010 support is dropped) will
    drop the Boost requirement.

- Swig.
  - Swig 1.x generates code that is no longer compatible with Python 3.x.
  - Swig 4.x should be used.


Building Boost on Windows
-------------------------

For the few libraries we need, the build is extremely quick.

- Download Boost 1.72.0 source code
- Run the following in _VS2015 x64 Native Tools Command Prompt_ (but note that
  even then `b2` will use the newest MSVC by default, so `toolset` must be
  specified explicitly if multiple VS versions are installed):
```
cd C:\local\boost_1_72_0
bootstrap
b2 --with-system --with-thread --with-date_time link=static runtime-link=shared toolset=msvc-14.0
```
- The above command builds both 32- and 64-bit versions, against both the Debug
  and Release MSVC runtimes.
- With MSVC, Boost headers will automatically select the libraries to link to,
  so we only need to set the paths.
- Pass these flags to `setup.py build_ext`:
  - `-IC:/local/boost_1_72_0`
  - `-LC:/local/boost_1_72_0/stage/lib`


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

- [Windows compiler versions for Python](https://wiki.python.org/moin/WindowsCompilers)
- [Building extensions for Python 3.5 part two](http://stevedower.id.au/blog/building-for-python-3-5-part-two/)
- [macOS compiler information](https://github.com/MacPython/wiki/wiki/Spinning-wheels)
- [manylinux build environment](https://github.com/pypa/manylinux)

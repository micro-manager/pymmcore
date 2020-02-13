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

- Swig 2.x should be used for now and must be on the path when running
  `setup.py`.


Building Boost on Windows
-------------------------

For the libraries we need, the build is extremely quick.

- Download Boost 1.72.0 source code
- Run the following in _x64 Native Tools Command Prompt for VS 2019_:
```
cd C:\local\boost_1_72_0
bootstrap
b2 --with-system --with-thread --with-date_time link=static runtime-link=shared
```
- The above command builds both 32- and 64-bit versions, against both the Debug
  and Release MSVC runtimes.
- With MSVC, Boost headers will automatically select the libraries to link to,
  so we only need to set the paths.
- Pass these flags to `setup.py build_ext`:
  - `-IC:/local/boost_1_72_0`
  - `-LC:/local/boost_1_72_0/stage/lib`


Resources
---------

- [Windows compiler versions for Python](https://wiki.python.org/moin/WindowsCompilers)
- [macOS compiler information](https://github.com/MacPython/wiki/wiki/Spinning-wheels)
- [manylinux build environment](https://github.com/pypa/manylinux)

## Versioning scheme

Cf. PEP 440.

Concatenate the MMCore version, MMDevice device interface version, and an extra
pymmcore-specific suffix. For example, pymmcore 10.1.1.69.0 wraps MMCore 10.1.1
and works with device adapters built for device interface version 69. The
final suffix can be incremented to create a new release for improvements to the
pymmcore wrapper.

```
pymmcore v10.1.1.69.0
          |      |  |
          |      |  +----> pymmcore-specific suffix
          |      +-------> MMDevice device interface version
          +--------------> MMCore version (major.minor.patch)
```

(Note that the device interface version can change without a change to the
MMCore version, although this is relatively uncommon. Also, we are leaving out
the module interface version, which rarely changes.)

The correspondence to MMCore and device interface versions is checked in
`tests/test_mmcore.py`.

Note that we can support multiple MMCore versions, possibly retroactively, by
maintaining separate branches; this can ease transition when the device
interface version changes. Such branches should be named `mmcore-x.y.z.w`.

When upgrading the MMCore version (by bumping the mmCoreAndDevices submodule
commit), the pymmcore version in `meson.build` should be updated in synchrony.
The versioning for the python package is taken dynamically from that file, via
the generated `_version.py` and the `project.dynamic` field in
`pyproject.toml`.

## Building Binary Wheels and Source Distributions

The package can be built in a few ways:

1. Use [cibuildwheel](https://cibuildwheel.readthedocs.io/en/stable/).
   This is the method used by the GitHub Actions CI workflow (configuration
   is in `pyproject.toml`). You can [run it locally](https://cibuildwheel.readthedocs.io/en/stable/setup/#local) as well
   if you have Docker installed:

    ```sh
    pip install cibuildwheel
    # example
    cibuildwheel --platform macos
    ```
   Or, to build a specific platform/python version:
   ```sh
   cibuildwheel --only cp310-macosx_x86_64
   ```

   The wheels will be placed in the `wheelhouse` directory.

2. Use the [build](https://pypi.org/project/build/) package

    ```sh
    pip install build
    python -m build
    ```

    This will build an sdist and wheel for the current platform and Python
    version, and place them in the `dist` directory.

3. Use `pip install --no-build-isolation -e .`
   This will build the extension module in-place and allow you to run tests,
   but will not build a wheel or sdist. `meson-python` (the build backend) will
   arrange to automatically rebuild the extension module each time it is
   imported. This method requires that you first manually install all of the
   build requirements listed in `pyproject.toml`. See the
   [meson-python docs](https://meson-python.readthedocs.io/en/latest/how-to-guides/editable-installs.html)
   for more information.

## Release procedure

Prepare two commits, one removing `.dev0` from the version and a subsequent one
bumping the patch version and re-adding `.dev0`. Tag the former with `v`
prefixed to the version:

```bash
git checkout main

vim meson.build  # Remove .dev0
git commit -a -m 'Version 1.2.3.42.4'
git tag -a v1.2.3.42.4 -m Release

vim meson.build  # Set version to 1.2.3.42.5.dev0
git commit -a -m 'Version back to dev'

git push upstream --follow-tags
git push
```

This triggers a build in [the ci.yml workflow](.github/workflows/ci.yml) and
the presence of a tag starting with "v" triggers a deployment to PyPI (using
[trusted publisher](https://docs.pypi.org/trusted-publishers/) authentication.)

Pushing the tag also creates a GitHub release with auto-generated release notes
and the binary wheels attached.

## Dependency and tool versions

- The minimum version of python supported is declared in `pypyproject.toml`,
  in the `[project.requires-python]` section.
- Meson (via `meson-python`), Ninja, and SWIG 4.x are required and
  automatically fetched via `pyproject.toml` under `[build-system.requires]`.
- A C++ toolchain is required and must be available on your system.
- The build-time versions of numpy are in `pyproject.toml`, in the
  `[build-system.requires]` section.
- The run-time numpy dependency is declared in `pyproject.toml`, in the
  `[project.dependencies]` section.
- Wheels are built with `cibuildwheel`, and the various wheel versions are
  determined by the settings in the `[tool.cibuildwheel]` section of
  `pyproject.toml`.
- _We_ should provide wheels for all Python versions we claim to support,
  built against the oldest NumPy version that we claim to support. Thus, any
  issue with the build or our CI will limit the lowest supported versions.

## ABI Compatibility

- The Python platform and ABI compatibility is all handled by the Wheel system.
  (But see below re MSVC versions.)

- NumPy ABI compatibility needs to be maintained by building against a
  reasonably old version of NumPy when packaging for public distribution (cf.
  https://github.com/numpy/numpy/issues/5888).  We do this by including
  [`oldest-supported-numpy`](https://github.com/scipy/oldest-supported-numpy)
  in our build requires.

### Legacy Build Notes

Many of these notes are probably obviated by the use of cibuildwheel... but
are kept for reference.

<details>

### Windows

- MSVC version. Python 3.5 and later are built with MSVC 14.x (i.e. Visual
  Studio 2015 to 2019). However, the official Python installer ships with its
  own copy of the VC runtime (in particular, `vcruntime140.dll`). This means
  that (in theory) our extension module must be built with an MSVC version that
  is not newer than the runtime shipped with Python. I say "in theory" because
  it is not clear if this actually results in problems, but let's play it safe.

  Python prints the MSVC version used to build itself when started. This
  version may change with the patch version of Python. Here are a few examples:

  - Python 3.8.1 (64-bit): MSC v.1916 = VS2017
  - Python 3.9.1 (64-bit): MSC v.1927 = VS2019
  - Python 3.8.7 (64-bit): MSC v.1928 = VS2019
  - Python 3.10.0 (64-bit): MSC v.1929 = VS2019
  - Python 3.11.0 (64-bit): MSC v.1933 = VS2022

  In general, it is probably safest to always build with VS2015 (older patch
  versions of Python 3.8 may be built with VS2015). This can be done by
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
- Our extension will still work if our deployment target is newer than
  Python's, so long as it is not newer than the host macOS version.
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


### Resources

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


</details>

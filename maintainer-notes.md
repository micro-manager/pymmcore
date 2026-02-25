# pymmcore development/maintainer notes

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

When upgrading the MMCore version (by updating the commit hashes in
`subprojects/mmdevice.wrap` and `subprojects/mmcore.wrap`), the pymmcore
version in `meson.build` must be updated in synchrony. The versioning for the
python package is taken dynamically from that file (by meson-python), and built
into the package via the generated `_version.py`.

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
   imported (this may poorly interact with caching if you are using uv). This
   method requires that you first manually install all of the build
   requirements listed in `pyproject.toml`. See the
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
- An appropriate C++ toolchain must be available on your system.
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

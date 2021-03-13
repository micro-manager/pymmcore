pymmcore: Python bindings for MMCore
====================================

The pymmcore package provides Python 3.x bindings to Micro-Manager's MMCore
(the low-level device control/acquisition interface).

Note: pymmcore is very similar to the legacy MMCorePy module (Python 2.x only),
distributed with the Micro-Manager application. However, the Python package for
pymmcore is named `pymmcore` instead of `MMCorePy`. This is in part to avoid
importing the wrong package on systems where `pymmcore` (usually installed via
`pip`) and `MMCorePy` (installed with the Micro-Manager app or built by the
user) both exist.

Because pymmcore is distributed separately from Micro-Manager, it needs to be
"pointed" at an existing Micro-Manager installation to access device adapters.
(See the example below.)


Installing
----------

Windows (Python 3.6-3.9), macOS (Python 3.6-3.9, 64-bit), and Linux (Python
3.6-3.9) are supported.

```
python -m pip install --user pymmcore
```
You can leave out the `--user` if installing into a virtual environment
(recommended).

Installation by `pip` should use binary wheels. If `pip` falls back to building
from source code, it will probably fail. If this happens in a supported
environment, please file a bug. To manually build from source, the scripts in
`.github/workflows` should serve as a starting point.

You also need a working installation of the Micro-Manager application.


Quick example
-------------

```python
import pymmcore
import os.path

mm_dir = "C:/Program Files/Micro-Manager-2.0beta"

mmc = pymmcore.CMMCore()
mmc.setDeviceAdapterSearchPaths([mm_dir])
mmc.loadSystemConfiguration(os.path.join(mm_dir, "MMConfig_demo.cfg"))

mmc.snapImage()
mmc.getImage()
```

We do not currently have Python-specific documentation for `CMMCore`. The [C++
documentation](https://valelab4.ucsf.edu/~MM/doc/MMCore/html/class_c_m_m_core.html)
is the best resource.


Matching Micro-Manager and pymmcore versions
--------------------------------------------

The version number of pymmcore is independent of the Micro-Manager version
number.

In order to use a given Micro-Manager installation, the _device interface
version_ must match between pymmcore and the Micro-Manager device adapters
(`mmgr_dal_*.dll` on Windows).

The device interface version of a given Micro-Manager installation can be
viewed in **Help** > **About Micro-Manager**.

The device interface version of a given pymmcore version is the fourth part in
the version number, and can also be viewed as follows:
```python
import pymmcore
pymmcore.CMMCore().getAPIVersionInfo()
```

Note that `getAPIVersionInfo()` should not be confused with `getVersionInfo()`,
which returns the version number of MMCore. (The MMCore version is the first 3
parts of the pymmcore version.)

- For example, pymmcore `10.1.1.69.0` is based on MMCore `10.1.1` and has
  device interface version `69`.
- The device interface version can change independently of the MMCore version,
  although it is less common for the device interface version to be incremented
  without a corresponding version change of MMCore.
- Older versions of pymmcore did not include the device interface version in
  their version number.

For a list of device interface versions for each pymmcore version, see the
[Releases](https://github.com/micro-manager/pymmcore/releases) page.


Loading device adapters on Windows
----------------------------------

The majority of device adapters should load once
`setDeviceAdapterSearchPaths()` has been called with the correct directories,
as in the above example. However, you may have trouble with device adapters
that in turn depend on external DLLs (typically equipment vendor libraries).

To fix this, _first ensure that the Micro-Manager application can correctly
load all the devices_ using the same configuration file. Then, use one of the
following:

- Temporarily change the current directory to the Micro-Manager installation
  when loading the configuration file (use `os.chdir()`).

- Add the Micro-Manager directory to the `PATH` environment variable.

The first method mimics how the Micro-Manager application works (it always run
with the current directory set to the installation directory). However, the
second method may be more robust in case the external DLLs in turn load
additional DLLs at a later time.

Please report any cases where the Micro-Manager application can load a
configuration but pymmcore cannot, even when using the above methods.


License
-------

The license for pymmcore itself is LGPL 2.1 (see `LICENSE.txt`). The MMCore
component of Micro-Manager (which gets built into pymmcore) is also under the
same license. Other parts of Micro-Manager are under different licenses.

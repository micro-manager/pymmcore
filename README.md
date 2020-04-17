pymmcore: Python bindings for MMCore
====================================

**Status**: Not available for `pip install` yet, but builds and works.

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

The following command **will** work once pymmcore is released:
```
python -m pip install --user pymmcore
```

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

The device interface version of a given pymmcore version can be viewed as
follows:
```python
import pymmcore
pymmcore.CMMCore().getAPIVersionInfo()
```

Note that `getAPIVersionInfo()` should not be confused with `getVersionInfo()`,
which returns the version number of MMCore. (The MMCore version is the first 3
parts of the pymmcore version.)

- For example, pymmcore `10.0.0.0` is based on MMCore `10.0.0`. That version of
  MMCore had device interface version `69`.
- Usually at least the last digit (patch version) of the MMCore version changes
  when there is a change to the device interface version.
- But several MMCore versions may share the same device interface version.


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

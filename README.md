Python bindings for MMCore
==========================

Status: Not ready for general use, although can be built on Windows.

This project is intended to become the standard build for Python bindings to
Micro-Manager's MMCore (the low-level device control/acquisition interface).

Note: pymmcore is very similar to the legacy MMCorePy module, distributed with
the Micro-Manager application. However, the Python package for pymmcore is
named `pymmcore` instead of `MMCorePy`. This is to avoid importing the wrong
package on systems where pymmcore (installed via `pip`) and `MMCorePy`
(installed with the Micro-Manager app or built by the user) both exist.

Because pymmcore is distributed separately from Micro-Manager, it needs to be
"pointed" at an existing Micro-Manager installation to access device adapters.
TODO Document how.


Versioning
----------

The version number of pymmcore is independent of the Micro-Manager version
number.

TODO Document how to select correct versions.


License
-------

The license for pymmcore itself is LGPL 2.1 (see `LICENSE.txt`). The MMCore
component of Micro-Manager (which gets built into pymmcore) is also under the
same license. Other parts of Micro-Manager are under different licenses.

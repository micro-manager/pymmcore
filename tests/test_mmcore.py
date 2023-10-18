import pymmcore


def test_core():
    # __version__ will be something like '10.4.0.71.1.dev0'
    pymmcore_version = pymmcore.__version__.split(".")

    mmc = pymmcore.CMMCore()
    
    # something like 'MMCore version 10.4.0'
    version_info = mmc.getVersionInfo()
    assert pymmcore_version[:3] == version_info.split()[-1].split(".")

    # something like 'Device API version 71, Module API version 10'
    api_version_info = mmc.getAPIVersionInfo()
    dev_interface_version = api_version_info.split(",")[0].split()[-1]
    assert pymmcore_version[3] == dev_interface_version

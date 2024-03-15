from unittest.mock import Mock

import pytest
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


@pytest.mark.skipif(pymmcore.POLYMORPHIC_MODE == 0, reason="POLYMORPHIC_MODE is 0")
def test_polymorphism():
    mock = Mock()

    class MySubCore(pymmcore.CMMCore):
        def setFocusDevice(self, focusLabel: str) -> None:
            mock(focusLabel)

    core = MySubCore()
    lbl = ""
    core.setProperty(pymmcore.g_Keyword_CoreDevice, pymmcore.g_Keyword_CoreFocus, lbl)
    mock.assert_called_once_with(lbl)

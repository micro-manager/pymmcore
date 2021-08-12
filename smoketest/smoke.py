import pymmcore


#
# At the moment, the only test is that our version numbering is correct
#

pymmcore_version = pymmcore.__version__.split('.')
print("Version: {}".format(pymmcore_version))

mmc = pymmcore.CMMCore()

# getVersionInfo() returns a string like "MMCore version 10.1.1"
mmcore_version = mmc.getVersionInfo().split()[-1].split('.')
print("MMCore version: {}".format(mmcore_version))

for i in range(3):
    if pymmcore_version[i] != mmcore_version[i]:
        raise AssertionError('Version mismatch between pymmcore and MMCore')


# getAPIVersionInfo() returns a string like
# "Device API version 69, Module API version 10"
dev_if_version = mmc.getAPIVersionInfo().split(',')[0].split()[-1]
mod_if_version = mmc.getAPIVersionInfo().split()[-1]
print("MMDevice device interface version: {}".format(dev_if_version))
print("MMDevice module interface version: {}".format(mod_if_version))

if pymmcore_version[3] != dev_if_version:
    raise AssertionError(
            'Version mismatch between pymmcore and device interface')

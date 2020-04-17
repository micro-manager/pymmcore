import pymmcore

import configparser
import os.path


#
# At the moment, the only test is that our version number is correct
#


script_dir = os.path.dirname(os.path.realpath(__file__))
setup_cfg = os.path.join(os.path.dirname(script_dir), 'setup.cfg')

config = configparser.ConfigParser()
config.read(setup_cfg)

pymmcore_version = config['metadata']['version'].split('.')
print("Version: {}".format(pymmcore_version))

# getVersionInfo() returns a string like "MMCore version x.y.z"
mmcore_version = pymmcore.CMMCore().getVersionInfo().split()[-1].split('.')
print("MMCore version: {}".format(mmcore_version))

for i in range(3):
    if pymmcore_version[i] != mmcore_version[i]:
        raise AssertionError('Version mismatch between pymmcore and MMCore')

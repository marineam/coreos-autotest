from autotest.client import test, utils
import dbus
import time
import os

success = False

class updateengine(test.test):
    version = 1

    def run_once(self, update_url="https://api.core-os.net/v1/update/"):
        utils.system("update_engine_client -omaha_url " + update_url)
	utils.system(self.srcdir + "/../../site_tests/updateengine/dbus")

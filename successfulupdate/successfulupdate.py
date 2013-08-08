from autotest.client import test, utils
import dbus
import time
import os

success = False

class successfulupdate(test.test):
    version = 1

    def run_once(self):
    	utils.system("mv /usr/local/autotest/tmp/site_tests/successfulupdate/reboottesting.service /media/state/units/")
	utils.system("sudo cgpt add -i 3 -P 5 /dev/sda")

	#TODO change to prod update service
	utils.system("update_engine_client -update -omaha_url http://192.168.122.1:8080/update")

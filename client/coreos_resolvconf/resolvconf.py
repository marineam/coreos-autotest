import os
from autotest.client import test, utils
class resolvconf(test.test):
    version = 1

    def run_once(self):
    	if not os.path.isfile('/etc/resolv.conf'):
	    raise Exception("/etc/resolv.conf does not exist")
	if not os.path.islink('/etc/resolv.conf'):
	    raise Exception("/etc/resolv.conf is not a symlink")

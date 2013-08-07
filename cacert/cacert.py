from autotest.client import test
import os
class cacert(test.test):
    version = 1


    def run_once(self):
        ca_path = "/usr/share/coreos-ca-certificates/"
    	if not os.path.isfile(ca_path + "CoreOS_Internet_Authority.pem"):
	    raise Exception("Missing CoreOS_Internet_Authority.pem")
	if not os.path.isfile(ca_path + "CoreOS_Network_Authority.pem"):
	    raise Exception("Missing CoreOS_Network_Authority.pem")

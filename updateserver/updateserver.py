from autotest.client import test, utils
class updateserver(test.test):
    version = 1


    def run_once(self):
        out = utils.system_output("curl -I http://api.core-os.net/v1/c10n/group | head -n 1|cut -d$' ' -f2")
	if out != '200':
	    raise Exception("Could not reach the update server")

from autotest.client import test, utils
import json
success = False

class etcd(test.test):
    version = 1

    def run_once(self, update_url="https://api.core-os.net/v1/update/"):
        utils.system('curl -L http://127.0.0.1:4001/v1/keys/message -d value="Hello world"')
	out = utils.system_output('curl -L http://127.0.0.1:4001/v1/keys/message')
	out_json = json.loads(out)
	if out_json["value"] != "Hello world":
		raise Exception("Value Mismatch")
	

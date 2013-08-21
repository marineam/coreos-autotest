from autotest.client import test, utils
class readonlyfs(test.test):
    version = 1


    def run_once(self):
        utils.system("mount | grep \"(r,\"")

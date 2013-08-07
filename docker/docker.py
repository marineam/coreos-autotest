from autotest.client import test, utils

class docker(test.test):
    version = 1

    def run_once(self, seconds=1):
        utils.system("docker run busybox echo")

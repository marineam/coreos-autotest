from autotest.client import test, utils
class sshtest(test.test):
    version = 1


    def run_once(self):
        utils.system("ssh 127.0.0.1 -l core -p 9222 << ENDHERE")

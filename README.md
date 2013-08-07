Coreos-Autotest
===============

This is a suite of tests to be used with the autotest framework in conjunction with CoreOS.

Setting up autotest with CoreOS
-------------------------------
Until we integrate autotest into our build process we setup autotest ourselves.

1. Create an autotest user in the chroot:
	```
	sudo useradd autotest
	sudo passwd autotest
	```
2. As root clone autotest into /usr/local/
	```
	sudo su -
	cd /usr/local
	git clone --resursive git://github.com/autotest/autotest.git
	```
3. Still as root, chown the new autotest dir to the autotest user:
	`chown -tR autotest:autotest /usr/local/autotest`

4. Give autotest a home dir and .ssh dir
	`mkdir -p /home/autotest/.ssh`

5. As autotest, create a passwordless ssh-key pair and copy it to the image
   	Boot your CoreOS VM, then
	```
	su autotest
	ssh-keygen -t rsa
	ssh-copy-id "core@127.0.0.1 -p 9222"
	Then enter the core user's password
	```
6. Testing should now work as the autotest user.  To confirm...
	```
	cd /usr/local/autotest
	server/autotest-remote -m 127.0.0.1 -c client/tests/sleeptest/control --ssh-user core --ssh-port 9222
	```
7. After this you're ready to clone the coreos tests:
	```
	cd /usr/local/autotest/client/
	git clone https://github.com/coreos/coreos-autotest.git
	```
8. To test this works:
	`server/autotest-remote -m 127.0.0.1 -c client/coreos-autotest/docker/control --ssh-user core --ssh-port 9222`


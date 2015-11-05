
#!/usr/bin/env python
# Name:    lepemtocrt.py
# Purpose:  Let's Encrypt PEM to CRT Script.
# By:       Jerry Gamblin
# Date:     04.11.15
# Modified  04.11.15
# Rev Level 0.5
# -----------------------------------------------

import os
import re
import time
import sys
import subprocess
import readline

#Make Dir to CRT
os.system("sudo mkdir -p ~/lecrt")

#Finding LetsEncrypt Cert
print "\n"
print "Found These LetsEncrypt Certs"
os.system('sudo ls -1 /etc/letsencrypt/live/')
print "\n"
os.system('sudo ls -1 /etc/letsencrypt/live/ > certs.txt')
c = open('certs.txt')
certs = c.read().splitlines()
c.close()
print "Converting .pem files to .crt"
for cert in certs: 
	cmd = 'sudo openssl x509 -outform der -in /etc/letsencrypt/live/'+cert+'/cert.pem -out ~/lecrt/'+cert+'.crt'
	os.system(cmd)
	print "You now have a %s.crt in ~/lecrt" % cert
os.system('sudo rm -rf certs.txt')
print "\n"

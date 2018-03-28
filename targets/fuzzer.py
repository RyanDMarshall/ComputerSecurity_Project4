#!/usr/bin/python
import subprocess
import os
import base64
import sys
import random
import string

testkey = "Key"
testint = "1"
testdoub = "1.0"
testchar = '0'
testarray = "[1,1,1]"

while True:
	testdoub = testdoub.replace('.','')
	testdoub = testdoub + str(random.randint(0,99999)) + "." + testdoub
	testobject = "{\"" + testkey + "\":\"" + testdoub + "\"}"


	child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	_, stdErrOut = child.communicate(input = testobject)
	if child.returncode != 0:
		print "Error: {}".format(child.returncode)
		print base64.b64encode(testobject)
		sys.exit(0)

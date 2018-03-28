#!/usr/bin/python
import subprocess
import os
import base64
import sys
from random import randint
from random import choice
import string

testkey = "Key"
testint = "1"
testdoub = "1.0"
testchar = '1'
teststr = "A"
testarray = "[1]"

iter = 0

while True and iter < 50:
	testdoub = testdoub.replace('.','')
	testdoub = testdoub + str(randint(0,99999)) + "." + testdoub
	testobject = "{\"" + testkey + "\":\"" + testdoub + "\"}"

	#testarrayleft = testarray.replace(']','')
	#testarrayright = testarray.replace('[','')
	#testarray = testarrayleft + "," + str(randint(0,9)) + "," + testarrayright
	#testobject = "{\"" + testkey + "\":\"" + testarray + "\"}"

	#testint = testint + str(randint(0,9)) + testint
	#testobject = "{\"" + testkey + "\":\"" + testint + "\"}"

	#teststr = teststr + choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) + teststr
	#testobject = "{\"" + testkey + "\":\"" + teststr + "\"}"

	child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
	_, stdErrOut = child.communicate(input = testobject)
	if child.returncode != 0:
		#print "ERROR: {}".format(child.returncode)
		print base64.b64encode(testobject)
		sys.exit(0)

	iter = iter + 1

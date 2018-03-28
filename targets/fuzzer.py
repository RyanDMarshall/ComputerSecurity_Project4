#!/usr/bin/python
import subprocess
import os
import base64
import sys

testCases = [
    '''{"a":"b\\""}''',
    '''{"a":"b"}''',
    '''{"a":["b",1]}''',
    '''{"asdf":"qwer","zxcv":[1,2,3,4],"fdsa":{"a":"b"}}''',
    '''{"a":1.234,"b":"c"}''',
    '''{"a":true,"b":false,"c":null}''',
    '''{"a":-1}''',
    '''{"a":"?"}''',
    '''{"a":"this is mult"}''',
    '''{"a mult":"t"}''',
    '''{ "a":"t"}''',
    '''{"a" :"t"}''',
    '''{"a": "t"}''',
    '''{"a":"t" }''',
    '''{"a":1E-4}''',
    '''{a}''',
    '''"asdf"''',
    '''{1:"a"}''',
    '''{"a:1}''',
    '''{"a":truetrue}''',
    '''{"a":1234.123.123}''',
    '''{"a":1E-4E-5}'''
]

for testcase in testCases :
    child = subprocess.Popen("./jsonParser", stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    _, stdErrOut = child.communicate(input = testcase)
    if child.returncode != 0 or stdErrOut != "" :
        print "|%s|" % stdErrOut
        sys.exit(0)

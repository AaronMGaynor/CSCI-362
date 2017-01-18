#!/usr/bin/env python

import os, sys

def testMul(x, y):

	#get Directory for functions and extract multiply
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import mul

	#run multiply function
	try:
		output = mul(int(x),int(y))
	except:
		output = "ERROR"
	
	return output



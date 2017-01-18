#!/usr/bin/env python

import os, sys

def testSub(x, y):

	#get Directory for functions and extract subtract function
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import sub

	#run subtract function
	try:
		output = sub(int(x),int(y))
	except:
		output = "ERROR"
	
	return output


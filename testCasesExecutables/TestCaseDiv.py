#!/usr/bin/env python

import os, sys

def testDiv(x, y):

	#get Directory for functions and extract divide
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import div

	#run divide function
	try:
		output = div(int(x),int(y))
	except:
		output = "ERROR"

	return output



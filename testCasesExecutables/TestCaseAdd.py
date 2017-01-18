#!/usr/bin/env python

import os, sys

def testAdd(x, y):

	#get Directory for functions and extract add function
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import add
	
	#run add function
	try:
		output = add(int(x),int(y))
	except:
		output = "ERROR"

	return output



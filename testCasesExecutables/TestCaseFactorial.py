#!/usr/bin/env python

import os, sys

def testFactorial(x):

	#get Directory for functions and extract factorial
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')
	currentworkingdirectory = (currentworkingdirectory + '/project/src')
	sys.path.insert(0, currentworkingdirectory)

	from functions import factorial

	#run factorial function
	try:
		output = factorial(int(x))
	except:
		output = "ERROR"
	
	return output



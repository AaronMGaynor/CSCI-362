#!/usr/bin/env python

import os,sys
import webbrowser

from TestCaseReader import testCaseExtractor
from outfile import intToText
from finalReportCreator import createReport
from cleaner import cleanTemps
from cleaner import cleanOutput

cleanTemps()
cleanOutput()
numberTestCases = 0

currentworkingdirectory = os.getcwd()
currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
currentworkingdirectory = currentworkingdirectory + '/testCasesExecutables'
sys.path.insert(0, currentworkingdirectory)

from TestCaseAdd import testAdd
from TestCaseDiv import testDiv
from TestCaseMul import testMul
from TestCaseSub import testSub
from TestCaseFactorial import testFactorial

currentworkingdirectory = currentworkingdirectory.replace('/testCasesExecutables', '')

for file in os.listdir((currentworkingdirectory + '/testCases')):
	if file.endswith(".txt"):
		numberTestCases = numberTestCases + 1

for i in range(1, (numberTestCases + 1)):
	
	#get current test case name & path
	currentTestCase = currentworkingdirectory + '/testCases/testCase' + str(i)
	currentOutFile = currentworkingdirectory + '/temp/testCaseOutput' + str(i)	

	#get method to be tested
	testCasei = open((currentTestCase + '.txt'), 'r')
	testCaseContents = testCasei.read()
	testCaseLines = testCaseContents.split('\n')
	methodToTest = testCaseLines[3]
	methodToTest = methodToTest.replace('Method: ', '')
	
	#run test
	if(methodToTest == 'add'):
		x, y = testCaseExtractor(currentTestCase)
		result = testAdd(x, y)
		intToText(currentOutFile, result)
	elif(methodToTest == 'mul'):
		x, y = testCaseExtractor(currentTestCase)
		result = testMul(x, y)
		intToText(currentOutFile, result)
	elif(methodToTest == 'div'):
		x, y = testCaseExtractor(currentTestCase)
		result = testDiv(x, y)
		intToText(currentOutFile, result)
	elif(methodToTest == 'sub'):
		x, y = testCaseExtractor(currentTestCase)
		result = testSub(x, y)
		intToText(currentOutFile, result)
	elif(methodToTest == 'factorial'):
		x = testCaseExtractor(currentTestCase)
		result = testFactorial(x)
		intToText(currentOutFile, result)
	else:
		print("INCORRECT METHOD TYPE: TEST CASE " + i)

#create final report
reportUrl = createReport(numberTestCases)
webbrowser.open_new_tab(reportUrl)
cleanTemps()

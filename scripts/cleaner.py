#!/usr/bin/env python

import os

def cleanTemps():
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
	currentworkingdirectory = currentworkingdirectory + '/temp'
	
	for file in os.listdir(currentworkingdirectory):
		if file.endswith(".txt"):
			os.remove(currentworkingdirectory + '/' + file)




def cleanOutput():
	currentworkingdirectory = os.getcwd()
	currentworkingdirectory = currentworkingdirectory.replace('/scripts', '')
	currentworkingdirectory = currentworkingdirectory + '/reports'

	for file in os.listdir(currentworkingdirectory):
		if file.endswith(".html"):
			os.remove(currentworkingdirectory + '/' + file)

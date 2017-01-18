def validator( oracleVal, actualVal):

	#test to see if reported values are acurate to expected values
	testVal = actualVal


	tempVal = oracleVal.split(" ")
	finalOracleVal = tempVal[2]
	if (finalOracleVal == testVal):
		return True
	else:
		return False


def intToText(filename, number):
	#create and populate output file
	f=open((filename +".txt"), 'w')
	f.write(str(number))
	f.close()


	

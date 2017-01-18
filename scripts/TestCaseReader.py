def testCaseExtractor(filename):
    #open and read test cases
    f=open((filename +".txt"), 'r')
    file_contents=f.read()
    file_contents=file_contents.split("\n")
    userNumbers=file_contents[4].split(" ")
    contentLength=len(userNumbers)

    if(contentLength==2):
        firstNum=userNumbers[1]
        return firstNum
    else:
        firstNum=userNumbers[1]
        secondNum=userNumbers[2]
        return firstNum, secondNum
        
    
    
    

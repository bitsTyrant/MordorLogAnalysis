def Serilialize():
    sFileName = "/Users/delta-5/Desktop/ModorLogAnalysis/Serilialization/covenant_dcsync_all_2019-10-27064128.json"
    try:
        sFile = open(sFileName) 
    except:
        print ('fail to open file: ', sFileName)
        return 
    tFileName = "../Serilialization/target_1.json"
    tFile = open(tFileName, "a")

    line = sFile.readline()
    line = '[' + line   
    num = 0         
    while line:
        num = num+1

        tempStr = line.split('{', 1)
        line = sFile.readline()

        if num%1000 == 0:
            tempLine = tempStr[0] + '{\"recordNo.\":' + str(num) + ',' + tempStr[1]
            tempLine = tempLine[:-1] + ']'
            tFile.write(tempLine)
            tFile.close()
            continue
        elif (num%1000 == 1)&(num != 1):
            tFileName = "../Serilialization/target_" + str(int(num/1000) + 1) + ".json"
            tFile = open(tFileName, "a")
            tempStr[0] = '[' + tempStr[0]

        if line:
            tempLine = tempStr[0] + '{\"recordNo.\":' + str(num) + ',' + tempStr[1]
            tempLine = tempLine[:-1] + ',\n'
            tFile.write(tempLine)

    if tFile:
        tempLine = tempStr[0] + '{\"recordNo.\":' + str(num) + ',' + tempStr[1]
        tempLine = tempLine[:-1] + ']'
        tFile.write(tempLine)
        tFile.close()
    
    sFile.close()

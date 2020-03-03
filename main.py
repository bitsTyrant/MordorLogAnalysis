from JsonSerialize import Serilialize
#from analyzeRecord import loadLine
import os

def echo():
    print ('======== M E N U =======')
    print ('1. 按照JSON标准, 格式化Mordor项目中small dataset中文件.')
    print ('2. ')
    print ('3. ')

if __name__ == "__main__":
    key = ''
    while key == '':
        echo()
        try:
            choice = int(input('select:\n'))
            if choice == 1:
                Serilialize()
            elif choice == 2:
                print ('fine')
            elif choice == 3:
                print ('good')
            else:
                print ('bad choice')
        except:
            print ('not optional')

        input('press ANY KEY to continue:')
        print ('\n\n\n\n')

    # sFileName = "/Users/delta-5/Desktop/jsonWork/RecordAnalysis/LogStack/covenant_dcsync_all_2019-10-27064128.json"
    # sFile = open(sFileName)

    # line = sFile.readline()
    # i = 0
    # while line:
    #     i = i + 1
    #     print (i, end=":\t")
    #     loadLine(line)
    #     line = sFile.readline()

    # sFile.close()
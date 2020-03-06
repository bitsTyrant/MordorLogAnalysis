import os
from json_serialization import serilialize
from log_structure_check import structure_check
from log_type_identify import type_identify
from log_type_identify import log_simplify
from log_type_info import log_name_valid

currentDir = '/covenant_dcsync_all/'
targetFileName = 'covenant_dcsync_all_2019-10-27064128.json'

def main_menu():
    print ('======== M E N U =======')
    print ('1. 按照JSON标准, 格式化Mordor项目中small dataset中文件.')
    print ('\tMordor')
    print ('2. 检查日志中是否存在不同的结构.')
    print ('3. 搜索日志库样本, 并检索新日志类别.并简化日志')
    print ('4. 选择新的日志类别')
    print ('5. 根据公共信息模型, 提取实体及实体关系.')
    print ('\t 目前公共信息模型包括三类:')
    print ('\t (1) 进程信息')
    print ('\t (2) 主机发生的动作')
    print ('\t (3) 登陆用户')
    print ('0. 退出')

'''
在主菜单中选择“4. 选择新的日志类别”以后弹出的子菜单
'''
def sub_menu_4():
    print ('请输入待查询的日志类别及编号. 格式为"事件类别_事件编号", 例如sysmon_10, winSec_4624')
    print ('输入“OFF”返回主菜单')

if __name__ == "__main__":
    while True:
        main_menu()
        try:
            choice = int(input('select:\n'))
            if choice == 1:
                serilialize(currentDir, targetFileName)
            elif choice == 2:
                path = os.path.abspath('./MordorLogAnalysis/LogStack/') + currentDir
                sFileName = path + targetFileName  
                
                try:
                    sFile = open(sFileName)
                except:
                    print ('fail to open file: ', sFileName)
                num = 0
                line = sFile.readline()
                while line:
                    num = num + 1
                    print (num)
                    structure_check(line, currentDir)
                    line = sFile.readline()
                sFile.close()

            elif choice == 3:
                type_identify(currentDir, targetFileName)
            elif choice == 4:   
                sub_menu_4()
                log_name = input('请输入:\n') 
                while log_name != 'OFF':
                    # 当log_name_valid(log_name)返回True的时候，补充分析的处理代码 
                    log_name_valid(log_name)
                    sub_menu_4()
                    log_name = input('请输入:\n')
            elif choice == 0:
                os._exit(0)
            else:
                print ('bad choice')
        except:
            print ('not optional')

        print ('\n\n\n\n')

    

    
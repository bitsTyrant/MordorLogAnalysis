import os
from arrange_by_type import sample_by_type

file_name = 'covenant_dcsync_all_2019-10-27064128.json'

def main_menu():
    print ('======== M E N U =======')
    print ('选项1. 按日志名称分类待分析文件, 并分析新出现的日志类别')
    print ('选项2. 压缩日志')
    print ('选项3. 根据公共信息模型，提取实体及实体关系. 目前公共信息模型包括三类:(1)进程信息; (2)主机发生的动作;(3)用户登陆会话期间的动作')
    print ('选项0. 退出')

def echo_1():
    print('\t\t按日志名称分类待分析文件:')
    print('\t\t\t将格式结构未识别的日志写入 abnormal')
    print('\t\t\t将日志类别未识别的日志写入 noval')
    print('\t\t\t已识别的日志类别写入 exist_type')
    print('\t\t\t未识别的日志类别写入 noval_type')
    print('\t\t\tlog_name由类别名称和编号组成, 类似 sysmon_3')
    print('\t\t\t将已识别的日志以日志名称为文件名 {log_name}, 写入 exist/{log_name}')
    print('\t\t\t将新类别的日志以日志名称为文件名 {log_name}, 写入 noval/{log_name}')
def option_1():
    sample_by_type(file_name)

'''
第二步: 
    对已识别的日志和新类别:
        获取日志结构的全集, 并写入 [exist|noval]/{log_name}_structure 文件
'''


'''
第一步:
    等待人工挑选 structure 文件中重要的属性
    按照 人工挑选的结果, 压缩文件
'''
def option_2():
    return True

if __name__ == '__main__':
    while True:
        main_menu()
        try: 
            choice = input('select:\n')
            if choice == '1':
                echo_1()
                option_1()
            elif choice == '2':
                echo_2()
                option_2()
            elif choice == '0':
                os._exit(0)
        except:
            print ('OK.')

        print ('\n\n\n\n')









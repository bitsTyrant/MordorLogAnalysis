import os
from arrange_by_type import sample_by_type
from type_schema import schema_analysis
from type_info import log_name_valid
from compress import compress

file_name = 'covenant_dcsync_all_2019-10-27064128.json'

def main_menu():
    print ('======== M E N U =======')
    print ('选项1. 按日志名称分类待分析文件, 并分析新出现的日志类别')
    print ('选项2. 压缩日志')
    print ('选项3. 根据公共信息模型，提取实体及实体关系. 目前公共信息模型包括三类:(1)进程信息; (2)主机发生的动作;(3)用户登陆会话期间的动作')
    print ('选项0. 退出')

'''
第一步:
    对目标文件进按照日志名称进行分为 abnormal 和 若干 log_name.json
第二步: 
    对已识别的日志和新类别:
        获取日志结构的全集, 并写入 [exist|noval]/{log_name}_schema 文件
'''
def echo_1():
    print('\t\t按日志名称分类待分析文件:')
    print('\t\t将格式结构未识别的日志写入 abnormal')
    print('\t\t将日志类别未识别的日志写入 noval')
    print('\t\t已识别的日志类别写入 exist_type')
    print('\t\t未识别的日志类别写入 noval_type')
    print('\t\tlog_name由类别名称和编号组成, 类似 sysmon_3')
    print('\t\t将已识别的日志以日志名称为文件名 {log_name}, 写入 exist/{log_name}')
    print('\t\t将新类别的日志以日志名称为文件名 {log_name}, 写入 noval/{log_name}')
def option_1():
    sample_by_type(file_name)
    schema_analysis()

def echo_2():
    print('请手动修改需要被压缩的日志所对应的 schema.yaml 文件')
    print('请输入需要被压缩的日志名称 log_name, 例如 sysmon_3')
    print('输入OFF返回主菜单')

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
                log_name = input('请输入:\n')
                while log_name != 'OFF':
                    if log_name_valid(log_name):
                        compress(log_name)
                        print(log_name+'类别日志已经压缩, 生成'+log_name+'.csv')
                    echo_2()
                    log_name = input('请输入:\n')
            elif choice == '0':
                os._exit(0)
        except:
            print ('OK.')

        print ('\n\n\n\n')

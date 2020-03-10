from type_check import type_check
from type_check import number_check

file_name = 'covenant_dcsync_all_2019-10-27064128.json'

from arrange_by_type import sample_by_type

sample_by_type(file_name)

'''
    打开待分析日志, 放入read_file
    使用字典 sample_by_type 存放按名称被分类的日志
        key 是文件的名称, 类似 sysmon_3
        value 是待写入的文本的列表
        sample_by_name初始化有两类 key : 'abnormal' 和 'noval'
    使用列表 exist_type 存放日志中所包含日志库中的日志名称
    使用列表 noval_type 存放日志中所包含新日志的日志名称

    逐行取出 read_file 的文本:
        将 line 转换为 json, 不能转换则写入 sample_by_type['abnoraml'] 
        使用 structure_check(json) 验证该行记录         
            如果不在标准结构列表中, 将 line 写入 sample_by_type['abnoraml']
        得到日志类型 type_name 和 日志编号 type_number
        使用 type_check(type_name)判断是否存在这种类型的日志
            如果不存在, 返回类型原文
                并将 type_name_type_number 存入noval_type
                将 line 写入 sample_by_type['noval']
            如果存在, 使用 number_check(type_name, type_number) 验证该行记录:
                如果不存在, 则将 type_name_type_number 存入noval_type
                    将 line 写入 sample_by_type['noval']
                如果 type_number 也在日志名列表中:
                    将 type_name_type_number 存入 exist_type
                    将 line 写入 sample_by_type['type_name_type_number']
        
        如果累计处理了5000行:
            依次遍历 sample_by_type 的 key 值
                如果 key 值为 abnormal, 则使用 write_log(abnormal_log, sample_by_name['abnormal'])
                如果 key 值为 noval, 则使用 write_log(noval_type_log, sample_by_name['noval'])
                否则, 使用 write_log(key的文件地址, sample_by_name[key])
            sample_by_type初始化为仅包含key: abnormal和noval
    
    将 sample_by_type 中剩下的值写入对应的文件中
    将 exist_type 写入 exist/exist_type 中
    将 noval_type 写入 noval/noval_type 中
'''
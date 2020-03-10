from type_info import type_name_mapping
from type_info import all_log_name

# 根据每行记录中的 日志名称 字段, 判断该类型日志是否入库
def type_check(type_name):
    if type_name in type_name_mapping.keys():
        return True
    else:
        return False

# 返回 日志名称 的缩写
def type_abbr(type_name):
    return type_name_mapping[type_name]

# 根据每行记录中的 日志名称 和 日志编号, 判断该类型日志是否入库
def number_check(type_name, type_number):
    if int(type_number) in all_log_name[type_name]:
        return True
    else:
        return False
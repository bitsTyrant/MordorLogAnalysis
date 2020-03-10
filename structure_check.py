import os
import json
from structure_info import log_structures

'''
    listIdentify()判断list_A与list_B包含元素是否完全相同的方法是：
    将list_A变换成集合A;
    将list_B变换成集合B;
    计算集合A和集合B的差集, 如果差集不为空, 那么判断list_A和list_B不相同;
    如果上一步差集为空, 则计算集合B与集合A的差集, 如果差集不为空, 则判断list_A和list_B不相同;
    如果上一步差集为空, 那么list_A与list_B所包含的元素完全相同。
'''
def listIdentify(listA, listB):
    setA = set(listA)
    setB = set(listB)
    difference = setA - setB
    if len(difference) != 0:
        return False
    difference  = setB - setA
    if len(difference) != 0:
        return False

    return True

def check_1(targetDict):
    ruler_dict = log_structures[0]
    if (not listIdentify(targetDict.keys(), ruler_dict['root'])):
        return False
    elif (not listIdentify(targetDict['ecs'].keys(), ruler_dict['ecs'])):
        return False
    elif (not listIdentify(targetDict['@metadata'].keys(), ruler_dict['@metadata'])):
        return False
    elif (not listIdentify(targetDict['host'].keys(), ruler_dict['host'])):
        return False
    elif (not listIdentify(targetDict['agent'].keys(), ruler_dict['agent'])):
        return False
    elif (not listIdentify(targetDict['log'].keys(), ruler_dict['log'])):
        return False
    elif (not listIdentify(targetDict['event'].keys(), ruler_dict['event'])):
        return False
    # elif (not listIdentify(targetDict['winlog'].keys(), ruler_dict['winlog'])):
    #     return False
    # elif (not listIdentify(targetDict['winlog']['user'].keys(), ruler_dict['user'])):
    #     return False
    # elif (not listIdentify(targetDict['winlog']['process'].keys(), ruler_dict['process'])):
    #     return False
    # elif (not listIdentify(targetDict['winlog']['process']['thread'].keys(), ruler_dict['thread'])):
    #     return False
    else:
        return True

def structure_check(line_to_json):
    if check_1(line_to_json):
        return 1
    else:
        return 0
        
# def structure_check(line, dir):
#     '''
#     分析该行日志是否为json格式。如果不是，将本行输入至异常样本文件abnormalLog中。
#     分析该行日志的Structure是否已经被记录。将本行输入至异常样本文件abnormalLog中。
#     '''
#     path = os.path.abspath('./MordorLogAnalysis/LogStack/') + dir
#     abnormalRecordFileName = path + ('abnormalRecord')
#     abnormalRecordFile = open(abnormalRecordFileName, 'a')
#     try:
#         json2Dict = json.loads(line)
#     except:
#         abnormalRecordFile.write(line)
#     else:
#         '''
#             如果符合第一种日志结构, 则返回编号1,
#             如果符合第二种日志结构, 则返回编号2,
#             ...
#             如果没有符合的日志结构, 则返回0
#         '''
#         if check_1(json2Dict):
#             return 1
#         else:
#             abnormalRecordFile.write(line)
#             return 0

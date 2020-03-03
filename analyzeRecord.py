import json

'''
一条日志里的属性名及其排列结构决定了日志的结构。
这里使用字典的k-v结构表示一条日志的结构。
k事先约定，对应的v是列表，代表json里面出现的属性名，顺序按照事先约定。
不同的日志结构用不同的字典表示，放在字典列表中LogStructure。
'''

eventSampleIdList = [3, 7, 9, 10, 11, 12, 18, 4624, 4627, 4634, 4662, 4672, 4703, 5140, 5156, 5158, 5145]
RootDictKeysSet = set(['@timestamp', '@metadata', 'host', 'ecs', 'agent', 'event', 'log', 'message', 'winlog'])
metadataDictKeysSet = set(['beat', 'type', 'version', 'topic'])
hostDictKeysSet = set(['name'])
hostEcsKeysSet = 
agentDictKeysSet = set(['hostname', 'id', 'ephemeral_id', 'type', 'version'])
winlogDictKeysSet = set(['computer_name', 'event_id', 'process', 'event_data', 'user', 'channel', 'opcode', 'provider_guid', 'version', 'record_id', 'task', 'api', 'provider_name'])

abnormalLogFileName = "/Users/delta-5/Desktop/jsonWork/RecordAnalysis/LogStack/abnormalLog"
abnormalLog = open(abnormalFileName, 'a')

def loadLine(line):
    # 
    '''
    分析该行日志是否为json格式。如果不是，将本行输入至异常样本文件abnormalLog中。
    分析该行日志的Structure是否已经被记录。将本行输入至异常样本文件abnormalLog中。
    分析该行日志所代表的日志类别是否已经被记录。将本行输入至异常样本文件abnormalLog中。   
    '''
    try:
        json2Dict = json.loads(line)
    except:
        abnormalLog.write(line)
    else:
        tempDictKeysSet = set(json2Dict.keys())
        DifferenceA = tempDictKeysSet - RootDictKeysSet
        DifferenceB = RootDictKeysSet - tempDictKeysSet
        if (len(DifferenceA) !=0 or len(DifferenceB) != 0):
            print ("================ **** ================")
            print ("current log has different structure: Root Dict different.")
            print (json2Dick.keys())
            print (line)
            print ("================ **** ================")
        else:
            print (json2Dict['winlog'].keys())

        if (json2Dict['event']['code'] not in eventSampleIdList):
            print (json2Dict['event']['code'])
            
            # createdStr = str(json2Dict['event']['created'])
            # kindStr = str(json2Dict['event']['kind'])
            # codeStr = str(json2Dict['event']['code'])
            # actionStr = str(json2Dict['event']['action'])
            # print (createdStr + '\t' + kindStr + '\t' + codeStr + '\t' + actionStr)

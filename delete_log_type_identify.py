
# import os
# import json
# import hashlib
# import csv
# from log_type_info import log_type_target_str
# from log_type_info import log_type_dict
# from log_type_info import log_schema







# '''
#     将待分析的目标原始日志中按照已经识别的日志类别检索一次
#         为存在的每种类别的日志建立一个文件，并放入一条样本数据
#         同时将所有尚未被收集的类别写入新的文件noval_log中
# '''
# def type_identify(dir, file_name):
#     iden_log_type = []
#     exist_type = []
#     noval_type = []
#     log_type_name_list = log_type_dict.keys()
#     for log_type_name in log_type_name_list:
#         for log_type_number in log_type_dict[log_type_name]:
#             iden_log_type.append(log_type_name + '_' + str(log_type_number))

#     path = os.path.abspath('./MordorLogAnalysis/LogStack/') + dir 
#     file_name = path + file_name    
#     target_file = open(file_name)

#     noval_log = open(path + 'noval_log/noval_log', 'w')
#     noval_type_file = open(path + 'noval_log/noval_type', 'a')

#     path = path + ('exist_classify/')
#     abnormal_record = open(path + 'abnormal_record', 'w')
    
#     line = target_file.readline()
#     while line:
#         try:
#             json2Dict = json.loads(line)
#         except:
#             abnormal_record.write('not a json. | ' + line)
#         else:
#             if (not 'winlog' in json2Dict.keys()):
#                 abnormal_record.write('have not winlog key. | ' + line)
#             elif (not 'provider_name' in json2Dict['winlog'].keys()):
#                 abnormal_record.write('have not provider_name key in winlog value. | ' + line)
#             else:
#                 type_name_str = json2Dict['winlog']['provider_name']
#                 if (type_name_str == 'Microsoft-Windows-Sysmon'):
#                     type_name = 'sysmon'
#                     if (not 'event_id' in json2Dict['winlog'].keys()):
#                         abnormal_record.write('have not event_id key in winlog value. | ' + line)
#                     else:
#                         type_number = json2Dict['winlog']['event_id']
                    
#                     file_name = type_name + '_' + str(type_number)
#                     if (not int(type_number) in log_type_dict['sysmon']):
#                         log_name = 'sysmon_' + str(type_number)
#                         if (not log_name in noval_type):
#                             noval_type.append(log_name)
#                             print (log_name)
#                         noval_log.write(line)
#                     elif (not file_name in exist_type):
#                         exist_type.append(file_name)
#                         exist_type_log = open(path+file_name, 'w')
#                         exist_type_log.write(line)
#                         exist_type_log.close()
#                 elif (type_name_str == 'Microsoft-Windows-Security-Auditing'):
#                     type_name = 'winSec'
#                     if (not 'event_id' in json2Dict['winlog'].keys()):
#                         abnormal_record.write('have not event_id key in winlog value. | ' + line)
#                     else:
#                         type_number = int(json2Dict['winlog']['event_id'])
                    
#                     file_name = type_name + '_' + str(type_number)
#                     if (not int(type_number) in log_type_dict['winSec']):
#                         log_name = 'winSec_' + str(type_number)
#                         if (not log_name in noval_type):
#                             noval_type.append(log_name)
#                             print (log_name)
#                         noval_log.write(line)
#                     elif (not file_name in exist_type):
#                         exist_type.append(file_name)
#                         exist_type_log = open(path+file_name, 'w')
#                         exist_type_log.write(line)
#                         exist_type_log.close()
#                 else:
#                     noval_log.write(line)

#         line = target_file.readline()

#     target_file.close()
#     abnormal_record.close()
#     noval_log.close()

#     for item in noval_type:
#         noval_type_file.write(item + '\n')

#     noval_type_file.close()


# '''
#     从指定的原始日志file中采样指定类别日志type的第一条日志,
#     并以该日志类别为文件名，在file同级别的目录中生成文件
#     文件中记录抽样的第一条日志
# '''
# def log_sample(path, file_name, log_name):
#     try:
#         read_file = open(path+file_name)
#     except:
#         print ('fail to open file: ' + file_name)
    
#     tmp_str = log_name.split('_')
#     log_type = tmp_str[0]
#     log_number = tmp_str[1]

#     target_log_str = log_type_target_str[log_type]

#     line = read_file.readline()
#     while line:
#         line2Dict = json.loads(line)
#         if (line2Dict['winlog']['provider_name'] == target_log_str) and (line2Dict['winlog']['event_id'] == int(log_number)):
#             print (path+log_name)
#             try:
#                 sample_file = open(path+log_name, 'w')
#                 print (sample_file)
#             except:
#                 print ('fail to create sample noval file.')

#             sample_file.write(line)
#             sample_file.close()
#             break

#         line = read_file.readline()        

# '''
#     对原始日志original_file中该类别log_type的日志进行化简
#     将结果写入目标文件夹下面的名为log_type的文件中
#     对每一类别日志该如何简化的依据写在log_type_info中。

# '''
# def log_simplify(read_filename, write_file_path, log_type):
#     try:
#         read_file = open(read_filename)
#     except:
#         print ('fail to open file: ' + read_filename)

#     log_type_schema = log_schema[log_type]
#     log_collection = {}

#     temp_str = log_type.split('_')
#     target_log_str = log_type_target_str[temp_str[0]]

#     md5 = hashlib.md5()
#     line = read_file.readline()
#     num = 0
#     while line:
#         json2Dict = json.loads(line)
#         if (json2Dict['winlog']['provider_name'] != target_log_str):
#             line = read_file.readline()
#             continue
#         elif (json2Dict['winlog']['event_id'] != int(temp_str[1])):
#             line = read_file.readline()
#             continue
#         else:
#             num = num + 1
#             # 按照事件在log_shema里面登记的信息, 将日志内容填充到original_record中
#             original_record = {}
#             for item in log_schema[log_type]:
#                 if item != 'hash_list':
#                     original_key_name = log_type_schema[item]
#                     tmp_str = original_key_name.split('.')
#                     temp_obj = json2Dict
#                     for key in tmp_str:
#                         temp_obj = temp_obj[key]
#                     original_record[item] = temp_obj
#             # 开始计算每一条记录的hash值. 如果两条记录hash值相同, 则进行归类
#             # 参与hash的字段在schema中确定.
#             to_be_hash_str = ''
#             for item in log_schema[log_type]['hash_list']:
#                 to_be_hash_str = to_be_hash_str + str(original_record[item])

#         md5.update(to_be_hash_str.encode('UTF-8'))
#         record_hash = md5.hexdigest()

#         # 以每条记录的hash值为key, 向log_collcetion里面填写记录
#         # 如果hash值相同，则合并为一簇, 并将未参与hash的字段放到日志的sequence中

#         if record_hash in log_collection.keys():
#             log_collection[record_hash]['timestamp'].append(original_record['timestamp'])
#             log_collection[record_hash]['record_number'].append(original_record['record_number'])
#             log_collection[record_hash]['beat'].append(original_record['beat'])
#             log_collection[record_hash]['agent_name'].append(original_record['agent_name'])
#         else:
#             original_record['timestamp'] = [original_record['timestamp']]
#             original_record['record_number'] = [original_record['record_number']]
#             original_record['beat'] = [original_record['beat']]
#             original_record['agent_name'] = [original_record['agent_name']]
#             log_collection[record_hash] = original_record
        
#         line = read_file.readline()

#     report = '\n\n\n\n' + str(num) + ' records TOTAL. \n' + str(len(log_collection)) + ' sequences TOTAL. '
#     with open(write_file_path + log_type, 'a') as report_file:
#         report_file.write(report)
#     report_file.close()

#     with open(write_file_path + log_type+'.csv', 'w') as csvfile:
#         writer = csv.writer(csvfile)
#         columns = []
#         columns = list(log_schema[log_type].keys())
#         columns.remove('hash_list')
#         writer.writerow(columns)
#         for log_key in log_collection.keys():
#             row = []
#             for item in columns:
#                 row.append(log_collection[log_key][item])

#             writer.writerow(row)

#     csvfile.close()

#     read_file.close() 
    
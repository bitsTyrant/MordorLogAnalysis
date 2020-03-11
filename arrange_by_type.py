import os
import json
from locate import get_root
from structure_check import structure_check
from type_check import type_check, type_abbr, number_check

MAX_COUNT = 1000

def write_to_file(sample, exist_type, noval_type):
    path = get_root()
    try:
        abnormal_file_name = os.path.join(path, 'abnormal.json')
        abnormal_file = open(abnormal_file_name, 'a')
    except:
        print('fail to open file: ' + abnormal_file_name)

    for line in sample['abnormal']:
        abnormal_file.write(line)
    abnormal_file.close()

    exist_type_base = os.path.join(path, 'exist_type')
    for log_name in exist_type:
        file_name = log_name + '.json'
        try:
            exist_type_file_name = os.path.join(exist_type_base, file_name)
            exist_type_file = open(exist_type_file_name, 'a')
        except:
            print('fail to open file: ' + exist_type_file_name)

        for line in sample[log_name]:
            exist_type_file.write(line)
        exist_type_file.close()

    noval_type_base = os.path.join(path, 'noval_type')
    for log_name in noval_type:
        file_name = log_name + '.json'
        try:
            noval_type_file_name = os.path.join(noval_type_base, file_name)
            noval_type_file = open(noval_type_file_name, 'a')
        except:
            print ('fail to open file: ' + noval_type_file_name)
        
        for line in sample[log_name]:
            noval_type_file.write(line)
        noval_type_file.close()

def sample_by_type(file_name):
    path = get_root()
    try:
        read_file_name = os.path.join(path, file_name)
        read_file = open(read_file_name)
    except:
        print ('fail to open file: ' + read_file_name)

    exist_type = []
    noval_type = []
    sample_by_type = {}
    sample_by_type['abnormal'] = []

    count = 0
    line = read_file.readline()
    while line:
        count = count+1
        if count % MAX_COUNT == 0:
            write_to_file(sample_by_type, exist_type, noval_type)
            print('------------  ' + str(count))
            print(noval_type)
            print(exist_type)
            for key in sample_by_type.keys():
                sample_by_type[key].clear()

        # line记录不是json格式, 加到 abnormal 中. 
        try:
            line_to_json = json.loads(line)
        except:
            sample_by_type['abnormal'].append(line)
            
            line = read_file.readline()
            continue

        '''
            下列三种情况, 将 line 写到 abnormal 中
            1. line 记录的结构不对;
            2. winlog 中 没有 provider_name 项;
            3. winlog中没有 event_id项  
        '''
        if structure_check(line_to_json) == 0:
            sample_by_type['abnormal'].append(line)
            line = read_file.readline()
            continue
        elif 'provider_name' not in line_to_json['winlog'].keys():
            sample_by_type['abnormal'].append(line)
            line = read_file.readline()
            continue
        elif 'event_id' not in line_to_json['winlog'].keys():
            sample_by_type['abnormal'].append(line)
            line = read_file.readline()
            continue

        type_name = line_to_json['winlog']['provider_name']
        type_number = line_to_json['winlog']['event_id']

        # 出现了新的日志类别, 将 line 加到 sample_by_type[log_name] 队列中
        if not type_check(type_name):
            log_name = type_name + '_' + str(type_number)
            if log_name not in noval_type:
                noval_type.append(log_name)
                sample_by_type[log_name] = []
                sample_by_type[log_name].append(line)
            else:
                sample_by_type[log_name].append(line)
            line = read_file.readline()
            continue

        # 出现了新的日志编号，将 line 加到 sample_by_type[log_name] 队列中
        type_name = type_abbr(type_name)
        if not number_check(type_name, type_number):
            log_name = type_name + '_' + str(type_number)
            if log_name not in noval_type:
                noval_type.append(log_name)
                sample_by_type[log_name] = []
                sample_by_type[log_name].append(line)
            else:
                sample_by_type[log_name].append(line)
            line = read_file.readline()
            continue
        
        # 日志名称已经在日志库中
        log_name = type_name + '_' + str(type_number)
        if not log_name in exist_type:
            exist_type.append(log_name)
            sample_by_type[log_name] = []
            sample_by_type[log_name].append(line)
        else:
            sample_by_type[log_name].append(line)
        
        
        line = read_file.readline()

    write_to_file(sample_by_type, exist_type, noval_type)

    # 将 exist_type 和 noval_type 写入根目录对应文件中
    file_name = os.path.join(path, 'exist_type_list')
    try:
        exist_type_list = open(file_name, 'a')
    except:
        print('fail to open file: ' + exist_type_list)

    for log_name in exist_type:
        exist_type_list.write(log_name + '\n')
    exist_type_list.close()

    file_name = os.path.join(path, 'noval_type_list')
    try:
        noval_type_list = open(file_name, 'a')
    except:
        print('fail to open file: ' + noval_type_list)

    for log_name in noval_type:
        noval_type_list.write(log_name + '\n')
    noval_type_list.close()

    return True

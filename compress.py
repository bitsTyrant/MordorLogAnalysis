import os, json, hashlib, csv
from ruamel import yaml
from locate import get_root

'''
人工挑选 schema 文件中的重要属性

选择选项2以后, 需要输入待压缩文件的 {log_name}
'''
def get_hash(log_dict, attr):
    to_be_hash_str = ''
    for key in attr:
        to_be_hash_str = to_be_hash_str + str(log_dict[key])
    md5 = hashlib.md5()
    md5.update(to_be_hash_str.encode('UTF-8'))
    return md5.hexdigest()

def value_by_key_path(log_dict, key_list):
    flatted_log = {}
    for key_path in key_list:
        sub_key = key_path.split('.')
        temp_obj = log_dict
        for item in sub_key:
            if item not in temp_obj.keys():
                temp_obj = '-'
                break
            temp_obj = temp_obj.get(item)
        flatted_log[key_path] = temp_obj
    return flatted_log
'''
log_collection 的填充方式如下:
    {
        %第一条日志的 MD5 值% : {
            'seq_attr': {
                %seq_attr[0]%: [%序列1对应日志中 %seq_attr[0]% 对应的值%, %序列2对应日志中 %seq_attr[0]% 对应的值%, ...],
                %seq_attr[1]%: [%序列1对应日志中 %seq_attr[1]% 对应的值%, %序列2对应日志中 %seq_attr[1]% 对应的值%, ...],
                ...
            },
            'hash_attr': {
                %hash_attr[0]%: %当前日志中 %hash_attr[0]% 对应的值%,
                %hash_attr[1]%: %当前日志中 %hash_attr[1]% 对应的值%,
                ...
            }
        },
        {第二条日志的 MD5 值} : {},
        {第三条日志的 MD5 值} : {},
        {第四条日志的 MD5 值} : {},
        ...
    }
    使用 value_by_key_path(line_to_json, seq_attr+hash_attr) 创建字典 flatted_log:
        {
            %seq_attr[0]%: ,
            %seq_attr[1]%: ,
            %seq_attr[2]%: ,
            ...
            %hash_attr[0]%: ,
            %hash_attr[1]%: ,
            %hash_attr[2]%: ,
            ... 
        }
    使用 get_hash(flatted_log, hash_attr) 计算每条日志对应的 hash 值
    如果 hash 值已经存在于 log_collection 的key中, 
        那么根据 seq_attr 里面的属性名, 按照属性名从 log_attr 中取值, 依次添加的属性对应的列表中
    否则, 新增一条字典记录, key是 hash 值, 
        创建字典 seq_attr_value :
            {
                %seq_attr[0]%: [],
                %seq_attr[1]%: [],
                %seq_attr[2]%: [],
                ...
            }
        取出 seq_attr 中的属性名, 从 log_attr 中获取日志中对应的属性值, 添加到字典 seq_attr_value 中
        创建字典 hash_attr_value :
            {
                %hash_attr[0]%: 
                %hash_attr[1]%: 
                %hash_attr[2]%:
                ...
            } 
'''
def compress(target_log_name):
    log_name_dict = {}
    log_name_dict['exist_type'] = []
    log_name_dict['noval_type'] = []
    exist_type_file_name = os.path.join(get_root(), 'exist_type_list')
    exist_type_file = open(exist_type_file_name)
    for log_name in exist_type_file:
        log_name_dict['exist_type'].append(log_name.rstrip())
    exist_type_file.close()
    noval_type_file_name = os.path.join(get_root(), 'noval_type_list')
    noval_type_file = open(noval_type_file_name)
    for log_name in noval_type_file:
        log_name_dict['noval_type'].append(log_name.rstrip())
    noval_type_file.close()

    if target_log_name in log_name_dict['exist_type']:
        log_type = 'exist_type'
    else:
        log_type = 'noval_type'

    schema_file_name = target_log_name + '_schema.yaml'
    schema_file_name = os.path.join(get_root(), log_type, schema_file_name)
    schema_file = open(schema_file_name, 'r', encoding='utf-8')
    schema = yaml.load(schema_file.read(), Loader=yaml.Loader)
    schema_file.close()

    compress_file_name = target_log_name + '_compress.csv'
    compress_file_name = os.path.join(get_root(), log_type, compress_file_name)

    seq_attr = schema['for_sequence']
    hash_attr = schema['for_compress']

    target_file_name = target_log_name + '.json'
    target_file_name = os.path.join(get_root(), log_type, target_file_name)
    target_file = open(target_file_name)

    log_collection = {}
    count = 0
    for line in target_file:
        count = count+1
        print('正在处理第 '+str(count)+' 条记录.')
        line_to_json = json.loads(line)
        flatted_log = value_by_key_path(line_to_json, seq_attr+hash_attr)
        hash_value = get_hash(flatted_log, hash_attr)

        if hash_value not in log_collection.keys():
            temp_seq_attr = {}
            for attr in seq_attr:
                temp_seq_attr[attr] = []
                temp_seq_attr[attr].append(flatted_log[attr])
            temp_hash_attr = {}
            for attr in hash_attr:
                temp_hash_attr[attr] = flatted_log[attr]
            
            log_collection[hash_value] = {}
            log_collection[hash_value]['seq_attr'] = temp_seq_attr
            log_collection[hash_value]['hash_attr'] = temp_hash_attr
        else:
            for attr in seq_attr:
                log_collection[hash_value]['seq_attr'][attr].append(flatted_log[attr])

    target_file.close()

    print('压缩文件路径: ' + compress_file_name)
    with open(compress_file_name, 'a') as csvfile:
        writer = csv.writer(csvfile)

        columns = seq_attr + hash_attr
        print('生成的表头为:' + str(columns))
        writer.writerow(columns)

        for hash_value in log_collection:
            row = []
            for attr in seq_attr:
                row.append(log_collection[hash_value]['seq_attr'][attr])
            for attr in hash_attr:
                row.append(log_collection[hash_value]['hash_attr'][attr])
            writer.writerow(row)
    csvfile.close()
    
import os, json
from ruamel import yaml
from locate import get_root

'''
根据字典 target 得到由所有key组成的列表 scheme
使用变长列表 scheme 保存字典 target 中所有的 key 的路径 key_path
将 target 的根 key, 放入scheme中
按顺序取出变长列表 scheme 的元素 key_path , 直到最后一个元素被处理:
    使用 . 切分 每个key_path, 得到 key[0].key[1].key[2]...
    通过 target[key[0]][key[1]...]获取对应的 value
    判断 value 是否为字典:
        如果是, 取出对应的 keys() 中的每一个 sub_key:
            key_path = key_path + '.' + sub_key
            将 key_path 添加到列表 scheme 的尾部 
'''
# obatin_scheme 还可以用来分析新结构日志的结构
def obtain_scheme(target):
    scheme = list(target.keys())
    for key_path in scheme:
        keys = key_path.split('.')
        tmp_obj = target
        for key in keys:
            tmp_obj = tmp_obj.get(key)
        if isinstance(tmp_obj, dict):
            for sub_key in tmp_obj.keys():
                tmp_key_path = key_path + '.' + sub_key
                scheme.append(tmp_key_path)

    return scheme

'''
将 scheme 写入 yaml 文件
'''
def write_to_yaml(scheme, file_name):
    waited_to_write = {}
    waited_to_write['original'] = scheme
    waited_to_write['omit'] = []
    waited_to_write['for_sequence'] = []
    waited_to_write['for_compress'] = []
    with open(file_name, 'w') as yaml_file:
        yaml.dump(waited_to_write, yaml_file, Dumper=yaml.RoundTripDumper)
    yaml_file.close()
    return True

'''
开始分析 exist_type 和 noval_type 这两个文件夹下面各 log_name 文件, 
获取各文件的结构 scheme, 写入 log_name.scheme 
'''
def scheme_analysis():
    category = ['exist_type', 'noval_type']
    for dir in category:
        file_name = os.path.join(get_root(), dir+'_list')
        to_obtain_scheme = []
        try:
            list_file = open(file_name)
        except:
            print('fail to open file: ' + file_name)

        line = list_file.readline()
        while line:
            to_obtain_scheme.append(line.rstrip())
            line = list_file.readline()
        
        path = os.path.join(get_root(), dir)
        for log_name in to_obtain_scheme:
            file_name = os.path.join(path, log_name+'.json')
            total_scheme = []
            
            try:
                read_file = open(file_name)
            except:
                print('fail to open: ' + file_name)
            
            for line in read_file:
                single_scheme = obtain_scheme(json.loads(line))
                for item in single_scheme:
                    if item not in total_scheme:
                        total_scheme.append(item)
            read_file.close()

            file_name = os.path.join(path, log_name+'.yaml')
            write_to_yaml(total_scheme, file_name)
    
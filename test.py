file_name = 'covenant_dcsync_all_2019-10-27064128.json'

from compress import value_by_key_path, get_hash, compress
from locate import get_root
import os
import json


# file_name = os.path.join(get_root(), 'noval_type', 'sysmon_3.json')
# file_name = os.path.join(get_root(), file_name)
# read_file = open(file_name)
# count = 0
# for line in read_file:
#     count = count + 1
    
#     line_to_json = json.loads(line)
#     print('-------------------' + str(count) + '-----------------------------')
#     temp_dict = value_by_key_path(line_to_json, data['for_sequence']+data['for_compress'])
#     for key in temp_dict.keys():
#         print(key + ': ' + str(temp_dict[key]))

#     print('HASH value is: '+get_hash(temp_dict, data['for_compress']))

# read_file.close()

compress('sysmon_3')
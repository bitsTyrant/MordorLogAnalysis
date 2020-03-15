'''
log_name = type_name + '-' + type_number
'''

type_name_mapping = {}
type_name_mapping['Microsoft-Windows-Sysmon'] = 'sysmon'
type_name_mapping['Microsoft-Windows-Security-Auditing'] = 'winSec'

all_log_name = {}
all_log_name['sysmon'] = [3]
all_log_name['winSec'] = []
# all_log_name['sysmon'] = [7, 9, 10, 11, 12, 18]
# all_log_name['winSec'] = [4627, 4634, 4662, 4672, 4703, 5140, 5145, 5156, 5158]

def log_name_valid(log_name):
    if (not '_' in log_name):
        print('-------- warning: --------')
        print('日志名称格式错误。正确的日志名称应该由日志类别和日志编号组成, 并使用\'_\'字符进行连接.')
        print('例如: sysmon_3, winSec_4624')
        return False
    else:
        tmp_str = log_name.split('_')
        if (not tmp_str[0] in all_log_name.keys()):
            print('-------- warning: --------')
            print ('日志类别错误. 目前日志类别为: ')
            for item in all_log_name.keys():
                print (item, end='    ')
            print ()
            return False
        elif (not int(tmp_str[1]) in all_log_name[tmp_str[0]]):
            print('-------- warning: --------')
            print ('日志编号错误. 目前', end='')
            print (tmp_str[0], end='')
            print ('类别的日志包含的事件类别为:')
            for item in all_log_name[tmp_str[0]]:
                print (item, end='  ')
            print ()
            print (tmp_str[0])
            print (tmp_str[1])
            return False
        else:
            return True
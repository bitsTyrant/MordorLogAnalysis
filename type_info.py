'''
log_name = type_name + '-' + type_number
'''

type_name_mapping = {}
type_name_mapping['Microsoft-Windows-Sysmon'] = 'sysmon'
type_name_mapping['Microsoft-Windows-Security-Auditing'] = 'winSec'

all_log_name = {}
all_log_name['sysmon'] = [7, 9, 10, 11, 12, 18]
all_log_name['winSec'] = [4627, 4634, 4662, 4672, 4703, 5140, 5145, 5156, 
                            5158]
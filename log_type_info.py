# 存储日志类别对应的检索字符串
log_type_target_str = {}
log_type_target_str['sysmon'] = 'Microsoft-Windows-Sysmon'
log_type_target_str['winSec'] = 'Microsoft-Windows-Security-Auditing'

log_type_dict = {}
#log_type_dict['sysmon'] = [3, 7, 9, 10, 11, 12, 18]
#log_type_dict['winSec'] = [4624, 4627, 4634, 4662, 4672, 4703, 5140, 5145, 5156, 5158]
log_type_dict['sysmon'] = [7, 9, 10, 11, 12, 18]
log_type_dict['winSec'] = [4627, 4634, 4662, 4672, 4703, 5140, 5145, 5156, 5158]

log_schema = {}

sysmon_3 = {}
sysmon_3['timestamp'] = 'winlog.event_data.UtcTime'
sysmon_3['record_number'] = 'winlog.record_id'
sysmon_3['beat'] = '@metadata.beat'
sysmon_3['agent_name'] = 'agent.hostname'
sysmon_3['provider_name'] = 'winlog.provider_name'
sysmon_3['action'] = 'event.action'
sysmon_3['level'] = 'log.level'
sysmon_3['host_name'] = 'winlog.computer_name'
sysmon_3['host_user_name'] = 'winlog.user.name'
sysmon_3['host_user_domain'] = 'winlog.user.domain'
sysmon_3['host_user_identifier'] = 'winlog.user.identifier'
sysmon_3['host_user_type'] = 'winlog.user.type'
sysmon_3['monitor_process_id'] = 'winlog.process.pid'
sysmon_3['monitor_thread_id'] = 'winlog.process.thread.id'
sysmon_3['source_image'] = 'winlog.event_data.Image'
sysmon_3['source_process_id'] = 'winlog.event_data.ProcessId'
sysmon_3['source_process_guid'] = 'winlog.event_data.ProcessGuid'
sysmon_3['source_protocol'] = 'winlog.event_data.Protocol'
sysmon_3['source_ip'] = 'winlog.event_data.SourceIp'
sysmon_3['source_port'] = 'winlog.event_data.SourcePort'
#sysmon_3['source_port_name'] = 'winlog.event_data.SourcePortName'
sysmon_3['source_is_ipv6'] = 'winlog.event_data.SourceIsIpv6'
sysmon_3['source_hostname'] = 'winlog.event_data.SourceHostname'
sysmon_3['source_user'] = 'winlog.event_data.User'
sysmon_3['initiated'] = 'winlog.event_data.Initiated'
sysmon_3['dest_ip'] = 'winlog.event_data.DestinationIp'
sysmon_3['dest_port'] = 'winlog.event_data.DestinationPort'
sysmon_3['dest_is_ipv6'] = 'winlog.event_data.DestinationIsIpv6'
#sysmon_3['dest_hostname'] = 'winlog.event_data.DestinationHostname'
sysmon_3['hash_list'] = ['provider_name', 'action', 'level', 'host_name', 'host_user_name', 'host_user_domain', 'host_user_identifier', 'host_user_type', 'monitor_process_id', 'monitor_thread_id', 'source_image', 'source_process_id', 'source_process_guid', 'source_protocol', 'source_ip', 'source_port', 'source_is_ipv6', 'source_hostname', 'source_user', 'initiated', 'dest_ip', 'dest_port', 'dest_is_ipv6']
log_schema['sysmon_3'] = sysmon_3

def log_name_valid(log_name):
    if (not '_' in log_name):
        print ('日志名称格式错误。正确的日志名称应该由日志类别和日志编号组成, 并使用\'_\'字符进行连接.')
        print ('例如: sysmon_3, winSec_4624')
        return False
    else:
        tmp_str = log_name.split('_')
        if (not tmp_str[0] in log_type_dict.keys()):
            print ('日志类别错误. 目前日志类别为: ')
            for item in log_type_dict.keys():
                print (item, end='    ')
            print ()
            return False
        elif (not int(tmp_str[1]) in log_type_dict[tmp_str[0]]):
            print ('日志编号错误. 目前', end='')
            print (tmp_str[0], end='')
            print ('类别的日志包含的事件类别为:')
            for item in log_type_dict[tmp_str[0]]:
                print (item, end='  ')
            print ()
            print (tmp_str[0])
            print (tmp_str[1])
            return False
        else:
            return True
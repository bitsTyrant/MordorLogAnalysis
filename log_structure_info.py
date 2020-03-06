'''
一条日志里的属性名及其排列结构决定了日志的结构。
这里使用字典的k-v结构表示一条日志的结构。
k事先约定，对应的v是列表，代表json里面出现的属性名，顺序按照事先约定。
不同的日志结构用不同的字典表示，放在字典列表中LogStructure。
'''

log_structure_sample = []
Structure_1 = {}
Structure_1['root'] = ['@timestamp', 'message', 'ecs', '@metadata', 'host', 'agent', 'log', 'event', 'winlog']
Structure_1['ecs'] = ['version']
Structure_1['@metadata'] = ['beat', 'version', 'type', 'topic']
Structure_1['host'] = ['name']
Structure_1['agent'] = ['hostname', 'id', 'version', 'type', 'ephemeral_id']
Structure_1['log'] = ['level']
Structure_1['event'] = ['created', 'kind', 'code', 'action']
# sysmon日志和Windows security日志从'winlog'所包含的字段开始有区别
Structure_1['winlog'] = ['provider_name', 'provider_guid', 'api', 'opcode', 'record_id', 'version', 'channel', 'event_id', 'computer_name', 'task', 'user', 'process', 'event_data']
Structure_1['user'] = ['domain', 'name', 'type', 'identifier']
Structure_1['process'] = ['thread', 'pid']
Structure_1['thread'] = ['id']
Structure_1['event_data'] = ['UtcTime', 'SourceProcessGUID', 'SourceProcessId', 'SourceThreadId', 'SourceImage', 'TargetProcessGUID', 'TargetProcessId', 'TargetImage', 'GrantedAccess', 'CallTrace']

log_structure_sample.append(Structure_1)
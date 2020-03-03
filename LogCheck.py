LogStructureSampleList = []
Structure_1 = {}
Structure_1['root'] = ['@timestamp', 'message', 'ecs', '@metadata', 'host', 'agent', 'log', 'event', 'winlog']
Structure_1['ecs'] = ['version']
Structure_1['@metadata'] = ['beat', 'version', 'type', 'topic']
Structure_1['host'] = ['name']
Structure_1['agent'] = ['hostname', 'id', 'version', 'type', 'ephemeral_id']
Structure_1['log'] = ['level']
Structure_1['event'] = ['created', 'kind', 'code', 'action']
Structure_1['winlog'] = ['provider_name', 'provider_guid', 'api', 'opcode', 'record_id', 'version', 'channel', 'event_id', 'computer_name', 'task', 'user', 'process', 'event_data']
Structure_1['user'] = ['domain', 'name', 'type', 'identifier']
Structure_1['process'] = ['thread', 'pid']
Structure_1['thread'] = ['id']
Structure_1['event_data'] = ['UtcTime', 'SourceProcessGUID', 'SourceProcessId', 'SourceThreadId', 'SourceImage', 'TargetProcessGUID', 'TargetProcessId', 'TargetImage', 'GrantedAccess', 'CallTrace']

LogStructureSampleList.append(Structure_1)

def StructureCheck(line):
    print (line)
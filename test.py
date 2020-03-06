import os
from log_type_identify import type_identify
from log_type_identify import log_sample
from log_type_identify import log_simplify

path = os.path.abspath('./MordorLogAnalysis/LogStack/')
currentDir = '/covenant_dcsync_all/'
targetFileName = 'covenant_dcsync_all_2019-10-27064128.json'

log_sample(path + currentDir + 'noval_log/', 'noval_log','sysmon_3')

log_simplify(path + currentDir + 'noval_log/noval_log', path + currentDir + 'noval_log/', 'sysmon_3')



import os

# 获取被分析文件的源文件的根目录绝对路径
def get_root():
    path = os.getcwd()
    return os.path.join(path, 'MordorLogAnalysis', 'log_pod')

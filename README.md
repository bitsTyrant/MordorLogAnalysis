# MordorLogAnalysis

1. log_pod为日志分析的根目录, 每次仅分析一个目标文件.

2. 将目标文件的文件名写到main.py的file_name变量中

3. 完成选项1的自动分类以后, 需要人工对每个日志的 scheme.yaml 文件进行选择. 不重要的字段填入omit中. 作为日志是否合并标志的字段填入for_compress. 剩下的字段填入 for_sequence 中, 仅作为合并后序列的展示.

4. 经过人工筛选之后的 scheme.yaml 文件是选项2日志合并操作的依据. 人工修改过某个log_name对应的scheme文件以后, 选择选项2, 然后输入{log_name}, 即可执行日志压缩的操作.
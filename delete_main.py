# '''
# 在主菜单中选择“4. 选择新的日志类别”以后弹出的子菜单
# '''
# def sub_menu_4():
#     print ('请输入待查询的日志类别及编号. 格式为"事件类别_事件编号", 例如sysmon_10, winSec_4624')
#     print ('输入“OFF”返回主菜单')

# if __name__ == "__main__":
#     while True:
#         main_menu()
#         try:
#             choice = int(input('select:\n'))
#             if choice == 1:
#                 option_1()
#             elif choice ==2:
#                 option_2()

#             # if choice == 1:
#             #     serilialize(currentDir, targetFileName)
#             # elif choice == 2:
#             #     path = os.path.abspath('./MordorLogAnalysis/LogStack/') + currentDir
#             #     sFileName = path + targetFileName  
                
#             #     try:
#             #         sFile = open(sFileName)
#             #     except:
#             #         print ('fail to open file: ', sFileName)
#             #     num = 0
#             #     line = sFile.readline()
#             #     while line:
#             #         num = num + 1
#             #         print (num)
#             #         structure_check(line, currentDir)
#             #         line = sFile.readline()
#             #     sFile.close()

#             # elif choice == 3:
#             #     type_identify(currentDir, targetFileName)
#             # elif choice == 4:   
#             #     sub_menu_4()
#             #     log_name = input('请输入:\n') 
#             #     while log_name != 'OFF':
#             #         # 当log_name_valid(log_name)返回True的时候，补充分析的处理代码 
#             #         log_name_valid(log_name)
#             #         sub_menu_4()
#             #         log_name = input('请输入:\n')
#             # elif choice == 0:
#             #     os._exit(0)
#             # else:
#             #     print ('bad choice')
#         except:
#             print ('not optional')

#         print ('\n\n\n\n')

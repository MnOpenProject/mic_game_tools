import os
from config import datacopy_remember_dir,auto_datacopy_remember_dir
from common_util import is_int_str
from eldenring_steam_copydata import main_action as copydata_main_action
from eldenring_steam_replacedata import main_action as replacedata_main_action
from eldenring_steam_replacedata_fromauto import main_action as replacedata_fromauto_main_action

def init_dirs():
    if not os.path.exists(datacopy_remember_dir):
        os.makedirs(datacopy_remember_dir)
    if not os.path.exists(auto_datacopy_remember_dir):
        os.makedirs(auto_datacopy_remember_dir)

if __name__ == "__main__":
    init_dirs()
    hint_options = [
        '游戏记录备份',
        '游戏记录还原 -- 从自己的备份目录进行还原',
        '游戏记录还原 -- 从自动备份目录进行还原（若想还原一个自己忘记备份的游戏记录，则使用这条）'
    ]
    funtion_list = [
        copydata_main_action,
        replacedata_main_action,
        replacedata_fromauto_main_action
    ]
    print('\n==================================\n')
    print('特别说明：还原游戏记录时，会默认把当前游戏记录自动备份到 auto_data_remember/ 文件夹下，万一哪次想还原一个自己忘记备份的游戏记录，则可以从这个文件夹下进行还原')
    for opt_i,opt in enumerate(hint_options):
        print(f'[{opt_i+1}] -- {opt}')
    user_select = input('请选择一个备份记录进行还原(输入对应编号即可)：')
    if not is_int_str(user_select) or int(user_select) > len(hint_options):
        print('输入有误，请输入对应的编号')
    else:
        select_idx =  int(user_select) - 1 # 用户选择项对应的索引值
        # 调用对应的函数
        funtion_list[select_idx]()
    


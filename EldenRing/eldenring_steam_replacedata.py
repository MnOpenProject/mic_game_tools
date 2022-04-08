''' 选用自己主动备份的游戏记录，覆盖游戏当前记录的脚本：即选择一个已备份的记录，复制到游戏记录的目录下，让游戏运行时进行使用 '''
import os,shutil,getpass,time
from config import datacopy_remember_dir,auto_datacopy_remember_dir
from common_util import del_files,is_int_str
from eldenring_steam_copydata import copydata_action

def init_dirs():
    if not os.path.exists(datacopy_remember_dir):
        os.makedirs(datacopy_remember_dir)
    if not os.path.exists(auto_datacopy_remember_dir):
        os.makedirs(auto_datacopy_remember_dir)

# 为 API 提供的功能函数
def replacedata_action_forapi(filename=None):
    # 获取当前系统登录用户名
    sys_user_name = getpass.getuser()
    print(f"系统信息:\n用户名 -- {sys_user_name}")
    # 通过用户名定位到游戏记录文件的存放目录
    game_data_root_dir = f"C:/Users/{sys_user_name}/AppData/Roaming"
    game_data_dir = f"{game_data_root_dir}/EldenRing"
    print(f'游戏记录文件的存放目录：{game_data_dir}')
    # 检查游戏记录文件的存放目录是否存在
    if not os.path.exists(game_data_dir):
        print(f'\n提醒：当前游戏不存在任何记录文件哦：{game_data_dir}')
        # return None
    # 判断是否已有备份的记录文件
    data_files = os.listdir(datacopy_remember_dir)
    if len(data_files) < 1:
        print(f'{datacopy_remember_dir}目录下，目前没有任何备份记录，请先备份记录')
        return None
    
    # # 选择一个备份记录，覆盖到当前的游戏记录
    # for cp_i,copyname in enumerate(data_files):
    #     print(f'[{cp_i+1}] -- {copyname}')
    # user_select = input('请选择一个备份记录进行还原(输入对应编号即可)：')
    # if not is_int_str(user_select) or int(user_select) > len(data_files):
    #     print('输入有误，请输入对应的编号')
    #     return None
    # select_idx =  int(user_select) - 1 # 用户选择的记录对应的索引值
    # 为了避免覆盖出现意外破坏了游戏记录，每次覆盖之前，都自动备份一份当前的游戏记录
    target_dir = copydata_action(output_dir=auto_datacopy_remember_dir,filename=time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())))
    print('\n==================================')
    print(f'{target_dir}\n游戏记录备份完成(自动备份功能)')
    # 先删除当前游戏的记录文件夹
    for i in range(2):
        del_files(game_data_dir)
    # 把当前选择的记录复制过去
    source_dir = f'{datacopy_remember_dir}/{filename}'
    print(f'当前选择的备份记录为: \n{source_dir}')
    target_dir = game_data_dir
    shutil.copytree(source_dir,target_dir)
    return target_dir

def replacedata_action():
    # 获取当前系统登录用户名
    sys_user_name = getpass.getuser()
    print(f"系统信息:\n用户名 -- {sys_user_name}")
    # 通过用户名定位到游戏记录文件的存放目录
    game_data_root_dir = f"C:/Users/{sys_user_name}/AppData/Roaming"
    game_data_dir = f"{game_data_root_dir}/EldenRing"
    print(f'游戏记录文件的存放目录：{game_data_dir}')
    # 检查游戏记录文件的存放目录是否存在
    if not os.path.exists(game_data_dir):
        print(f'\n提醒：当前游戏不存在任何记录文件哦：{game_data_dir}')
        # return None
    # 判断是否已有备份的记录文件
    data_files = os.listdir(datacopy_remember_dir)
    if len(data_files) < 1:
        print(f'{datacopy_remember_dir}目录下，目前没有任何备份记录，请先备份记录')
        return None
    
    # 选择一个备份记录，覆盖到当前的游戏记录
    for cp_i,copyname in enumerate(data_files):
        print(f'[{cp_i+1}] -- {copyname}')
    user_select = input('请选择一个备份记录进行还原(输入对应编号即可)：')
    if not is_int_str(user_select) or int(user_select) > len(data_files):
        print('输入有误，请输入对应的编号')
        return None
    select_idx =  int(user_select) - 1 # 用户选择的记录对应的索引值
    # 为了避免覆盖出现意外破坏了游戏记录，每次覆盖之前，都自动备份一份当前的游戏记录
    target_dir = copydata_action(output_dir=auto_datacopy_remember_dir,filename=time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time())))
    print('\n==================================')
    print(f'{target_dir}\n游戏记录备份完成(自动备份功能)')
    # 先删除当前游戏的记录文件夹
    for i in range(2):
        del_files(game_data_dir)
    # 把当前选择的记录复制过去
    source_dir = f'{datacopy_remember_dir}/{data_files[select_idx]}'
    print(f'当前选择的备份记录为: \n{source_dir}')
    target_dir = game_data_dir
    shutil.copytree(source_dir,target_dir)
    return target_dir

def main_action():
    target_dir = replacedata_action()
    if not target_dir == None:
        print('\n==================================')
        print(f'{target_dir}\n游戏记录还原完成')
    

if __name__ == "__main__":
    init_dirs()
    main_action()

''' 游戏备份脚本 '''
import os,shutil,getpass,time
from config import datacopy_remember_dir

def init_dirs():
    if not os.path.exists(datacopy_remember_dir):
        os.makedirs(datacopy_remember_dir)

def copydata_action(output_dir=None,filename=None):
    # 获取当前系统登录用户名
    sys_user_name = getpass.getuser()
    print(f"系统信息:\n用户名 -- {sys_user_name}")
    # 通过用户名定位到游戏记录文件的存放目录
    game_data_dir = f"C:/Users/{sys_user_name}/AppData/Roaming/EldenRing"
    print(f'游戏记录文件的存放目录：{game_data_dir}')
    # 检查游戏记录文件的存放目录是否存在
    if not os.path.exists(game_data_dir):
        print(f'\n游戏记录文件的存放目录不存在：{game_data_dir}')
        return None
    # 判断是否已有记录文件
    data_files = os.listdir(game_data_dir)
    # print(data_files)
    # 排除 .xml 文件，剩下的就是记录文件的文件夹
    data_files = [i for i in data_files if not '.xml' in i]
    # print(data_files)
    if len(data_files) < 1:
        print(f'{game_data_dir}目录下，目前没有任何记录文件，请先进行游戏吧')
        return None

    # 把当前游戏记录复制出来
    copyname = ''
    if filename == None:
        copyname_input = input('请输入要备份记录的名称: ')
        time_str = time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time()))
        copyname = f'{copyname_input}__{time_str}'
    else: 
        copyname = filename
    print(copyname)
    source_dir = game_data_dir
    target_dir = f'{datacopy_remember_dir}/{copyname}' if output_dir == None else f'{output_dir}/{copyname}'

    shutil.copytree(source_dir,target_dir)
    return target_dir

def main_action():
    target_dir = copydata_action()
    if not target_dir == None:
        print('\n==================================')
        print(f'{target_dir}\n游戏记录备份完成')

if __name__ == "__main__":
    init_dirs()
    main_action()

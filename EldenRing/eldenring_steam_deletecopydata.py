''' 删除备份数据 '''
import shutil
from config import datacopy_remember_dir,auto_datacopy_remember_dir

# 为 API 提供的功能函数
def deletecopydata_action_forapi(filename):
    gamecopydata_dir = f'{datacopy_remember_dir}/{filename}'
    # 删除备份记录文件夹
    print(f'删除记录文件夹： {gamecopydata_dir}')
    shutil.rmtree(gamecopydata_dir)

def deletecopydata_fromauto_action_forapi(filename):
    gamecopydata_dir = f'{auto_datacopy_remember_dir}/{filename}'
    # 删除备份记录文件夹
    print(f'删除自动记录文件夹： {gamecopydata_dir}')
    shutil.rmtree(gamecopydata_dir)



# import os,shutil

# 判定是否为纯整数字符串
def is_int_str(str):
    try:
        int(str)
        return True
    except:
        return False

# # 删除一个文件夹下的所有文件
# def del_files(dir):
#     shutil.rmtree(dir)
import os

# 判定是否为纯整数字符串
def is_int_str(str):
    try:
        int(str)
        return True
    except:
        return False

# 删除一个文件夹下的所有文件
def del_files(path,dir=None):
    try:
        print(f'正在删除...\n{path}')
        try:
            if not dir == None and os.path.exists(dir):
                os.removedirs(dir)
        except Exception as ex:
            # print(f'del_files ex = {ex}')
            pass
        if os.path.exists(path):
            ls = os.listdir(path)
            count = len(ls)
            for n,i in enumerate(ls):
                print(f'删除进度：{n+1}/{count}')
                c_path = os.path.join(path, i)
                if os.path.isdir(c_path):
                    del_files(c_path,c_path)
                else:
                    os.remove(c_path)
    except Exception as er:
        del_files(path)
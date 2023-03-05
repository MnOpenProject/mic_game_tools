# flask打包成exe可执行文件参考资料：https://bbs.huaweicloud.com/blogs/210229
# 执行该脚本，把当前flask工程打包成exe可执行文件
import os

# 当前脚本所在根目录
__CURPATH__ = str(os.path.abspath(
    os.path.dirname(__file__))).replace('\\', '/')

# 需要被打包的文件夹
# 若后续有啥变化，记得要这里更改哦
package_dirs = [
    'templates',
    'static',
    'auto_data_remember',
    'data_remember'
]

# 打包时需要排除掉的文件（即不需要被打包输出的文件）
# 若后续有啥变化，记得要这里更改哦
package_not_output_files = ['out_to_exe.py','__init__.py']

# 删除一个文件夹下的所有文件


def del_files(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_files(c_path)
            try:
                os.removedirs(c_path)
            except:
                print('')
        else:
            os.remove(c_path)


def clearOut_dirs():
    build_dir = '{}/build'.format(__CURPATH__)
    dist_dir = '{}/dist'.format(__CURPATH__)
    spec_file = '{}/start.spec'.format(__CURPATH__)
    if os.path.exists(build_dir):
        del_files(build_dir)
    if os.path.exists(dist_dir):
        del_files(dist_dir)
    if os.path.exists(spec_file):
        os.remove(spec_file)

# 读取需要被打包的所有文件（非文件夹）
def read_all_py():
    cur_file_list = os.listdir(__CURPATH__)
    cur_need_out_py = [x for x in cur_file_list if x[-3:] == '.py' and x not in package_not_output_files]
    return cur_need_out_py

if __name__ == '__main__':
    clearOut_dirs()
    package_files = read_all_py()

    # cmd_str = 'pyinstaller -F start.py'
    # cmd_str = 'pyinstaller -F start.spec'

    cmd_str = 'pyinstaller -F -i icon.ico'
    for dir_path in package_dirs:
        cmd_str = '{0} --add-data="{1};{1}"'.format(cmd_str, dir_path)
    for file_path in package_files:
        cmd_str = '{0} --add-data="{1};."'.format(cmd_str, file_path)
    cmd_str = '{0} start.py'.format(cmd_str)
    print(cmd_str)
    # cmd_str = 'pyinstaller -F -i icon.ico --add-data="轮回修仙路修改器\lhxx_config;轮回修仙路修改器\lhxx_config" --add-data="轮回修仙路修改器\lhxx_editor_scripts;轮回修仙路修改器\lhxx_editor_scripts" --add-data="轮回修仙路修改器\lhxx_flask_app;轮回修仙路修改器\lhxx_flask_app" --add-data="start.py;." start.py'
    os.system(cmd_str)

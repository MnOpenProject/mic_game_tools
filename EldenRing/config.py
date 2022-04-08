import socket
# 存放备份记录的文件夹
datacopy_remember_dir = "data_remember"
# 自动存放备份记录的文件夹（每次还原记录时会自动把当前游戏记录自动备份到这个目录下，如果当前游戏记录被破坏了，可以从这个文件夹下还原回去）
auto_datacopy_remember_dir = "auto_data_remember"

# 获取当前服务器的 IP
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
# 服务器启动的 IP
server_ip = get_host_ip()
# 服务启动的端口号
server_port = 5555
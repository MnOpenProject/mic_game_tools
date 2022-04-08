import os,sys,socket
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)
from config import server_ip,server_port
from route import app

if __name__ == '__main__':
    from livereload import Server
    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve(host=server_ip,port=server_port)
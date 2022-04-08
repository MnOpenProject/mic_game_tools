import os,sys
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_PATH)
from route import app

# print("http://127.0.0.1:{}".format(SERVER_PORT))

if __name__ == '__main__':
    from livereload import Server
    server = Server(app.wsgi_app)
    server.watch('**/*.*')
    server.serve()
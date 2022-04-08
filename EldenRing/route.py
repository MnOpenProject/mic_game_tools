
import os,json,time
from flask import request, render_template
from flask_app import app
from config import datacopy_remember_dir,auto_datacopy_remember_dir,server_ip,server_port
from eldenring_steam_copydata import copydata_action
from eldenring_steam_replacedata import replacedata_action_forapi
from eldenring_steam_replacedata_fromauto import replacedata_fromauto_action_forapi
from eldenring_steam_deletecopydata import deletecopydata_action_forapi,deletecopydata_fromauto_action_forapi

def init_dirs():
    if not os.path.exists(datacopy_remember_dir):
        os.makedirs(datacopy_remember_dir)
    if not os.path.exists(auto_datacopy_remember_dir):
        os.makedirs(auto_datacopy_remember_dir)

@app.route('/')
def index():
    init_dirs()
    # 获取主动备份记录列表
    user_datacopy_list = os.listdir(datacopy_remember_dir)
    user_datacopy_list = user_datacopy_list[::-1] # 倒序排列，让时间最早的数据显示在第一条
    # 获取自动备份记录列表
    auto_datacopy_list = os.listdir(auto_datacopy_remember_dir)
    auto_datacopy_list = auto_datacopy_list[::-1] # 倒序排列，让时间最早的数据显示在第一条
    return render_template('index.html',user_datacopy_list=user_datacopy_list,auto_datacopy_list=auto_datacopy_list,server_ip=server_ip,server_port=server_port)


@app.route('/copygamedata',methods =['get'])
def copygamedata_api():
    copyname_input = request.args.get("filename")
    time_str = time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time()))
    copyname = f'{time_str}__{copyname_input}'
    target_dir = copydata_action(filename=copyname)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

@app.route('/replacegamedata',methods =['get'])
def replacegamedata_api():
    filename = request.args.get("filename")
    target_dir = replacedata_action_forapi(filename=filename)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

@app.route('/replacegamedatafromauto',methods =['get'])
def replacegamedatafromauto_api():
    filename = request.args.get("filename")
    target_dir = replacedata_fromauto_action_forapi(filename=filename)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

@app.route('/deletegamedata',methods =['get'])
def deletegamedata_api():
    filename = request.args.get("filename")
    target_dir = deletecopydata_action_forapi(filename=filename)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

@app.route('/deletegamedatafromauto',methods =['get'])
def deletegamedatafromauto_api():
    filename = request.args.get("filename")
    target_dir = deletecopydata_fromauto_action_forapi(filename=filename)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

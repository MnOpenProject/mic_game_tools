
import os,json,time
from flask import request, render_template
from flask_app import app
from config import datacopy_remember_dir,auto_datacopy_remember_dir
from eldenring_steam_copydata import copydata_action
from eldenring_steam_replacedata import replacedata_action_forapi

@app.route('/')
def index():
    # 获取主动备份记录列表
    user_datacopy_list = os.listdir(datacopy_remember_dir)
    # 获取自动备份记录列表
    auto_datacopy_list = os.listdir(auto_datacopy_remember_dir)
    return render_template('index.html',user_datacopy_list=user_datacopy_list,auto_datacopy_list=auto_datacopy_list)


@app.route('/copygamedata',methods =['get'])
def getVideoSeasons_api():
    copyname_input = request.args.get("filename")
    time_str = time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time()))
    copyname = f'{copyname_input}__{time_str}'
    target_dir = copydata_action(filename=copyname)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)

@app.route('/replacegamedata',methods =['get'])
def getVideoSeasons_api():
    copyname_input = request.args.get("filename")
    time_str = time.strftime(r'%Y年%m月%d日%H时%M分%S秒',time.localtime(time.time()))
    copyname = f'{copyname_input}__{time_str}'
    target_dir = copydata_action(filename=copyname)

    response = {
        'code': 200,
        'data': target_dir
    }
    return json.dumps(response)
    # username = request.json.get("username")
    # password = request.json.get("password")
    # return '{"msg": "你已经登录", "code": 800}'
    # password = md5_passwd(password)
    # if username and password:
    #     r1 = redis.Redis(host= MYRDS_HOST, port= MYRDS_PORT, password='123456', db=RDS_DB)
    #     keys = r1.keys()
    #     if username.encode() in keys:
    #             return '{"msg": "你已经登录", "code": 800}'
    #     else:
    #         sql = 'select id,username,password from user where username ="%s";' % username
    #         res = conn_mysql(sql)
    #         if not res:
    #             return '{code":200,"msg":"用户名不存在}'
    #         elif res['password'] == password:
    #             r1.setex(username,1,1000)
    #             return '{"code":200,"msg":"登录成功"}'
    #         else:
    #             return '{"code":400,"msg":"密码输入错误"}'
    # else:
    #     return my_json(NOT_NULL)
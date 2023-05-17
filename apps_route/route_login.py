import json
from flask import request, jsonify
from apps import user_login
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_login = Blueprint('route_login', __name__)


@route_login.route('/user_table/login', methods=['POST'])
def login():
    """
    前端传入数据转化字典示例：
    {"user_name": "vivi", "user_secret": "123456"}
    :return: json数据(传入也是json数据)
    """
    return user_login().login_result(JsonUtil().to_Object()['user_name'],
                                     JsonUtil().to_Object()['user_secret'])


@route_login.route('/user_table/register', methods=['POST'])
def register():
    """
    前端传入数据示例：{"user_name": "vivi", "user_secret": "123456"}
    :return:
    """
    # 1.获取前端json数据
    data = request.get_data()
    json_data = json.loads(data)
    # print(data)
    # print(json_data)
    username = json_data.get("user_name")
    password = json_data.get("user_secret")
    # 2.数据处理,注册用户
    user = user_login()
    canregister, beizhu = user.register(username, password)
    # 3.给前端传输json数据
    info = dict()
    info['status'] = canregister
    info['beizhu'] = beizhu
    # info['time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(info)

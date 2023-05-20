from apps import AppPublic
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_public = Blueprint('route_public', __name__)


@route_public.route('/public/login', methods=['POST'])
def login():
    """
    用户登陆接口
    input: {"username": "", "password": ""}
    :return: {'状态': "成功"/"失败", '提示信息': "", "用户类型": ""}
    """
    return AppPublic().login_result(JsonUtil().to_Object()['username'],
                                    JsonUtil().to_Object()['password'])


@route_public.route('/public/register', methods=['POST'])
def register():
    """
    用户注册接口
    input: {"username": "", "password": ""}
    :return: {'状态': "成功"/"失败", '提示信息': ""}
    """
    return AppPublic().register_result(JsonUtil().to_Object()['username'],
                                       JsonUtil().to_Object()['password'])


@route_public.route('/public/updatePassword', methods=['POST'])
def updatePassword():
    """
    用户密码修改接口
    input: {"usertype": "", "username": "", "newPassword": ""}
    :return: {'状态': "成功"/"失败", '提示信息': ""}
    """
    return AppPublic().updatePassword_result(JsonUtil().to_Object()['usertype'],
                                             JsonUtil().to_Object()['username'],
                                             JsonUtil().to_Object()['newPassword'])

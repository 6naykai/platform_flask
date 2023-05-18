from apps import AppPublic
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_public = Blueprint('route_public', __name__)


@route_public.route('/public/login', methods=['POST'])
def login():
    return AppPublic().login_result(JsonUtil().to_Object()['username'],
                                    JsonUtil().to_Object()['password'])


@route_public.route('/public/register', methods=['POST'])
def register():
    return AppPublic().register_result(JsonUtil().to_Object()['username'],
                                       JsonUtil().to_Object()['password'])


@route_public.route('/public/updatePassword', methods=['POST'])
def updatePassword():
    return AppPublic().updatePassword_result(JsonUtil().to_Object()['usertype'],
                                             JsonUtil().to_Object()['username'],
                                             JsonUtil().to_Object()['newPassword'])

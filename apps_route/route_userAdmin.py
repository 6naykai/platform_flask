from apps import AppUserAdmin
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_userAdmin = Blueprint('route_userAdmin', __name__)


@route_userAdmin.route('/userAdmin/usersSelectPassword', methods=['POST'])
def usersSelectPassword():
    return AppUserAdmin().usersSelectPassword_result()


@route_userAdmin.route('/userAdmin/usersSelectFlag', methods=['POST'])
def usersSelectFlag():
    return AppUserAdmin().usersSelectFlag_result()


@route_userAdmin.route('/userAdmin/userInsert', methods=['POST'])
def userInsert():
    return AppUserAdmin().userInsert_result(JsonUtil().to_Object()['userName'],
                                            JsonUtil().to_Object()['userPassword'],
                                            JsonUtil().to_Object()['userFlag'])


@route_userAdmin.route('/userAdmin/userUpdatePassword', methods=['POST'])
def userUpdatePassword():
    return AppUserAdmin().userUpdatePassword_result(JsonUtil().to_Object()['userName'],
                                                    JsonUtil().to_Object()['newPassword'])


@route_userAdmin.route('/userAdmin/userUpdateForbidden', methods=['POST'])
def userUpdateForbidden():
    return AppUserAdmin().userUpdateForbidden_result(JsonUtil().to_Object()['userName'],
                                                     JsonUtil().to_Object()['newFlag'])


@route_userAdmin.route('/userAdmin/userDelete', methods=['POST'])
def userDelete():
    return AppUserAdmin().userDelete_result(JsonUtil().to_Object()['userName'])

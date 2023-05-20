from apps import AppRootAdmin
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_rootAdmin = Blueprint('route_rootAdmin', __name__)


@route_rootAdmin.route('/rootAdmin/accountsSelectPassword', methods=['POST'])
def accountsSelectPassword():
    return AppRootAdmin().accountsSelectPassword_result()


@route_rootAdmin.route('/rootAdmin/accountsSelectType', methods=['POST'])
def accountsSelectType():
    return AppRootAdmin().accountsSelectType_result()


@route_rootAdmin.route('/rootAdmin/accountInsert', methods=['POST'])
def accountInsert():
    return AppRootAdmin().accountInsert_result(JsonUtil().to_Object()['accountName'],
                                               JsonUtil().to_Object()['accountPassword'],
                                               JsonUtil().to_Object()['accountType'])


@route_rootAdmin.route('/rootAdmin/accountUpdatePassword', methods=['POST'])
def accountUpdatePassword():
    return AppRootAdmin().accountUpdatePassword_result(JsonUtil().to_Object()['accountName'],
                                                       JsonUtil().to_Object()['newPassword'],
                                                       JsonUtil().to_Object()['accountType'])


@route_rootAdmin.route('/rootAdmin/adminUpdateType', methods=['POST'])
def adminUpdateType():
    return AppRootAdmin().adminUpdateType_result(JsonUtil().to_Object()['adminName'],
                                                 JsonUtil().to_Object()['adminType'])


@route_rootAdmin.route('/rootAdmin/accountDelete', methods=['POST'])
def accountDelete():
    return AppRootAdmin().accountDelete_result(JsonUtil().to_Object()['accountName'],
                                               JsonUtil().to_Object()['accountType'])

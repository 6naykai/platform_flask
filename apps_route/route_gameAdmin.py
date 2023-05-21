from apps import AppGameAdmin
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_gameAdmin = Blueprint('route_gameAdmin', __name__)


@route_gameAdmin.route('/gameAdmin/gamesSelectGamePath', methods=['POST'])
def gamesSelectGamePath():
    return AppGameAdmin().gamesSelectGamePath_result()


@route_gameAdmin.route('/gameAdmin/gamesSelectIsAdded', methods=['POST'])
def gamesSelectIsAdded():
    return AppGameAdmin().gamesSelectIsAdded_result()


@route_gameAdmin.route('/gameAdmin/gameUpdateIsAdded', methods=['POST'])
def gameUpdateIsAdded():
    return AppGameAdmin().gameUpdateIsAdded_result(JsonUtil().to_Object()['gameName'],
                                                   JsonUtil().to_Object()['newIsAdded'])


@route_gameAdmin.route('/gameAdmin/gameDelete', methods=['POST'])
def gameDelete():
    return AppGameAdmin().gameDelete_result(JsonUtil().to_Object()['gameName'])


@route_gameAdmin.route('/gameAdmin/gameUpload', methods=['POST'])
def gameUpload():
    dataDict = JsonUtil().uploadFile_to_Object()
    print(dataDict)
    fileName = dataDict["文件名称"]
    filePath = dataDict["文件路径"]
    fileType = dataDict["文件类型"]
    return AppGameAdmin().gameUpload_result(fileName, filePath, fileType)

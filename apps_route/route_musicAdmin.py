from apps import AppMusicAdmin
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_musicAdmin = Blueprint('route_musicAdmin', __name__)


@route_musicAdmin.route('/musicAdmin/musicsSelectMusicPath', methods=['POST'])
def musicsSelectMusicPath():
    return AppMusicAdmin().musicsSelectMusicPath_result()


@route_musicAdmin.route('/musicAdmin/musicsSelectIsAccretion', methods=['POST'])
def musicsSelectIsAccretion():
    return AppMusicAdmin().musicsSelectIsAccretion_result()


@route_musicAdmin.route('/musicAdmin/musicUpdateIsAccretion', methods=['POST'])
def musicUpdateIsAccretion():
    return AppMusicAdmin().musicUpdateIsAccretion_result(JsonUtil().to_Object()['musicName'],
                                                         JsonUtil().to_Object()['newIsAccretion'])


@route_musicAdmin.route('/musicAdmin/musicDelete', methods=['POST'])
def musicDelete():
    return AppMusicAdmin().musicDelete_result(JsonUtil().to_Object()['musicName'])


@route_musicAdmin.route('/musicAdmin/musicUpload', methods=['POST'])
def musicUpload():
    dataDict = JsonUtil().uploadFile_to_Object()
    print(dataDict)
    fileName = dataDict["文件名称"]
    filePath = dataDict["文件路径"]
    fileType = dataDict["文件类型"]
    return AppMusicAdmin().musicUpload_result(fileName, filePath, fileType)

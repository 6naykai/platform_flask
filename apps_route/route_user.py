from apps import AppUser
from flask import Blueprint
from util import JsonUtil

# 构建蓝本
route_user = Blueprint('route_user', __name__)


@route_user.route('/user/musicInit', methods=['POST'])
def musicInit():
    """
    音乐列表初始化接口
    input: None
    :return: {musicName:musicPath,....}
    """
    return AppUser().musicInit_result()


@route_user.route('/user/musicDownload/<filepath>', methods=['POST'])
def musicDownload(filepath):
    """
    音乐下载接口
    :param filepath: 下载文件绝对路径
    :return: 返回下载Response对象
    """
    return AppUser().musicDownload(filepath)


@route_user.route('/user/gameInit', methods=['POST'])
def gameInit():
    """
    游戏列表初始化接口
    input: None
    :return: {gameName:gamePath,....}
    """
    return AppUser().gameInit_result()


@route_user.route('/user/gameDownload/<filepath>', methods=['POST'])
def gameDownload(filepath):
    """
    游戏下载接口
    :param filepath: 下载文件绝对路径
    :return: 返回下载Response对象,设置好了'Content-Length'供后端读取
    """
    return AppUser().gameDownload(filepath)

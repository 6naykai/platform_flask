import os
from flask import Response
from flask import Blueprint
from settings import MUSIC_DOWNLOAD_PATH

# 构建蓝本
route_download = Blueprint('route_download', __name__)


# 文件下载
@route_download.route('/download/<filetype>/<filename>', methods=['POST'])
def download(filetype, filename):
    """
    下载接口
    :param filetype: 下载文件类型
    :param filename: 下载文件名称(包含后缀)
    :return: 下载对象
    """
    # 音乐文件下载函数
    def music_download():
        # path = os.path.dirname(os.path.abspath(__file__))
        path = MUSIC_DOWNLOAD_PATH + filename
        with open(path, 'rb') as fmp3:
            data = fmp3.read(1024)
            while data:
                yield data
                data = fmp3.read(1024)
    if filetype == 'music':
        return Response(music_download(), mimetype="audio/mpeg3")

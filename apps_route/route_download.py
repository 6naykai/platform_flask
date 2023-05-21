import os
import uuid
from pypinyin import lazy_pinyin
from flask import Response, request
from flask import Blueprint
from werkzeug.utils import secure_filename

from settings import MUSIC_DOWNLOAD_PATH, GAME_DOWNLOAD_PATH, UPLOADTEST_PATH

# 构建蓝本
route_download = Blueprint('route_download', __name__)


@route_download.route('/upload', methods=['GET', 'POST'])
def upload():
    # file为上传表单的name属性值
    f = request.files['file']
    # filename = secure_filename(''.join(lazy_pinyin(file.filename)))
    fname = secure_filename(''.join(lazy_pinyin(f.filename)))
    print(fname)
    ext = fname.rsplit('.')[-1]
    print(ext)
    ffname = fname.rsplit('.')[0]
    print(ffname)
    # 生成一个uuid作为文件名
    fileName = str(uuid.uuid4()) + "." + ext
    # os.path.join拼接地址，上传地址，f.filename获取文件名
    f.save(os.path.join(UPLOADTEST_PATH, fileName))
    return 'ok'


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

    # exe文件下载函数
    def exe_download():
        # path = os.path.dirname(os.path.abspath(__file__))
        path = GAME_DOWNLOAD_PATH + filename
        with open(path, 'rb') as fexe:
            data = fexe.read(1024)
            while data:
                yield data
                data = fexe.read(1024)
    if filetype == 'music':
        return Response(music_download(), mimetype="audio/mpeg3")
    if filetype == 'game':
        filePath = GAME_DOWNLOAD_PATH + filename
        fsize = os.path.getsize(filePath)
        response = Response(exe_download(), mimetype="application/octet-stream")
        response.headers['Content-Length'] = fsize
        return response

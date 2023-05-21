import json
import os
import re
import uuid
from settings import UPLOAD_MUSIC_PATH, UPLOAD_GAME_PATH, UPLOADTEST_PATH
from flask import request
from werkzeug.utils import secure_filename


class JsonUtil:
    def __init__(self):
        self.__jsonData = None
        self.__file = None
        self.__fileName = None
        self.__fileType = None

    def to_Object(self):
        self.__jsonData = request.get_data()
        json_data = json.loads(self.__jsonData)
        return json_data

    def uploadFile_to_Object(self):
        """
        上传文件的函数,此时对象只能创建一个
        :return: 字典,用于给music_table插入数据
        """
        self.__file = request.files['file']
        print(self.__file)
        # self.__fileData = request.get_data()
        # print(self.__file.filename)
        # re.findall正则获取音乐名称
        music_name = re.findall(r'(.+?)\.mp3', re.findall(r'[^\\/:*?"<>|\r\n]+$', self.__file.filename)[0])[0]
        print(music_name)
        fileName = secure_filename(self.__file.filename)
        self.__fileName = music_name  # 文件原来的名字
        self.__fileType = fileName.rsplit('.')[-1]
        # 生成一个uuid作为文件名
        fileName = str(uuid.uuid4()) + "." + self.__fileType
        # os.path.join拼接地址，上传地址，f.filename获取文件名
        UPLOAD_PATH = UPLOADTEST_PATH + fileName
        if self.__fileType == 'mp3':
            UPLOAD_PATH = os.path.join(UPLOAD_MUSIC_PATH, fileName)
        elif self.__fileType == 'exe':
            UPLOAD_PATH = os.path.join(UPLOAD_GAME_PATH, fileName)
        self.__file.save(UPLOAD_PATH)
        return {"文件名称": self.__fileName,
                "文件路径": UPLOAD_PATH,
                "文件类型": self.__fileType}

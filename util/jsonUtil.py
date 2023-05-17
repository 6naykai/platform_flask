import json

from flask import request


class JsonUtil:
    def __init__(self):
        self.__jsonData = None

    def to_Object(self):
        self.__jsonData = request.get_data()
        json_data = json.loads(self.__jsonData)
        return json_data

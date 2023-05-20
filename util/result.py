from flask import jsonify


class Result:
    def __init__(self, state, information, data=None):
        """
        对于结果的包装类Result
        :param state: 操作状态,成功/失败
        :param information: 返回的提示信息,用于前端提示框
        :param data: 需传回前端的信息dict型,dict中内容是str型的键值对,可为空
        """
        self.__state = state
        self.__information = information
        self.__data = data

    def to_Json(self):
        info = dict()
        if self.__data is not None:
            for key, value in self.__data.items():
                info[key] = value
        # 如果传值不涉及状态和提示信息
        if self.__state is None:
            return jsonify(info)
        info['状态'] = self.__state
        info['提示信息'] = self.__information
        return jsonify(info)

import abc


# 数据库接口的抽象基类
class AbstractInterface(abc.ABC):
    def __init__(self):
        self.__DATABASE = None
        self.__USER = None
        self.__PASSWORD = None
        self.__URL = None
        self.__PORT = None

    @abc.abstractmethod
    def create_conn(self):
        pass

    @abc.abstractmethod
    def ExecuSQL(self, argv):
        pass

    @abc.abstractmethod
    def getData(self, argv):
        pass

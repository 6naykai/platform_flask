import abc


# 用户的抽象基类
class AbstractUser(abc.ABC):
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @abc.abstractmethod
    def get_username(self):
        return self.__username

    @abc.abstractmethod
    def set_username(self, username):
        self.__username = username

    @abc.abstractmethod
    def get_password(self):
        return self.__password

    @abc.abstractmethod
    def set_password(self, password):
        self.__password = password

    @abc.abstractmethod
    def ToString(self):
        pass

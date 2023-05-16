import abc


# 用户的抽象基类
class AbstractUser(abc.ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @abc.abstractmethod
    def get_username(self):
        return self.username

    @abc.abstractmethod
    def set_username(self, username):
        self.username = username

    @abc.abstractmethod
    def get_password(self):
        return self.password

    @abc.abstractmethod
    def set_password(self, password):
        self.password = password

    @abc.abstractmethod
    def ToString(self):
        pass

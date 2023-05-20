from .abstract_user import AbstractUser


class User(AbstractUser):
    def __init__(self, username: str, password: str, flag=False, surplus=3):
        super().__init__(username, password)
        self.__username = username
        self.__password = password
        self.__flag = flag
        self.__surplus = surplus

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_flag(self):
        return self.__flag

    def set_flag(self, flag):
        self.__flag = flag

    def get_surplus(self):
        return self.__surplus

    def set_surplus(self, surplus):
        self.__surplus = surplus

    def ToString(self):
        return "user_table{" + \
               "user_name=" + str(self.__username) + \
               ", user_secret=" + str(self.__password) + \
               ", user_forbidden=" + str(self.__flag) + \
               ", user_surplus=" + str(self.__surplus) + \
               "}"


if __name__ == '__main__':
    a = User(1, 1, False, 3)
    print(a.ToString())

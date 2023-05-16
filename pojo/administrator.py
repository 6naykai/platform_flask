from .abstract_user import AbstractUser


class Administrator(AbstractUser):
    def __init__(self, username, password, admin_type):
        super().__init__(username, password)
        self.__username = username
        self.__password = password
        self.__admin_type = admin_type

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password

    def set_password(self, password):
        self.__password = password

    def get_type(self):
        return self.__admin_type

    def set_type(self, admin_type):
        self.__admin_type = admin_type

    def ToString(self):
        return "administrator_table{" + \
               "administrator_name=" + str(self.__username) + \
               ", administrator_secret=" + str(self.__password) + \
               ", administrator_type=" + str(self.__admin_type) + \
               "}"

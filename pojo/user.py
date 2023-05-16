from pojo import AbstractUser


class User(AbstractUser):
    def __init__(self, username, password, flag, surplus):
        super().__init__(username, password)
        self.flag = flag
        self.surplus = surplus

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_flag(self):
        return self.flag

    def set_flag(self, flag):
        self.flag = flag

    def get_surplus(self):
        return self.surplus

    def set_surplus(self, surplus):
        self.surplus = surplus

    def ToString(self):
        return "user_table{" + \
               "user_name=" + str(self.username) + \
               ", user_secret=" + str(self.password) + \
               ", user_forbidden=" + str(self.flag) + \
               ", user_surplus=" + str(self.surplus) + \
               "}"


if __name__ == '__main__':
    a = User(1, 1, 1, 3)
    print(a.ToString())

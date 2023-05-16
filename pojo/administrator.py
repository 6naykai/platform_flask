from pojo import AbstractUser


class Administrator(AbstractUser):
    def __init__(self, username, password, admin_type):
        super().__init__(username, password)
        self.admin_type = admin_type

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_type(self):
        return self.admin_type

    def set_type(self, admin_type):
        self.admin_type = admin_type

    def ToString(self):
        return "administrator_table{" + \
               "administrator_name=" + str(self.username) + \
               ", administrator_secret=" + str(self.password) + \
               ", administrator_type=" + str(self.admin_type) + \
               "}"

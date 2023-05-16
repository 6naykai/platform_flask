from .database_interface import openGauss


# 用户表接口类: user_table
class Database_user:
    def __init__(self):
        self.database_interface = openGauss()

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def select(self):
        pass

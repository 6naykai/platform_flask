from database import Database_user, Database_administrator
from pojo import User, Administrator


class AppImplRootAdmin:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.data = {}              # 数据传输字典
        self.__database_user = Database_user()
        self.__database_admin = Database_administrator()

    def accountsSelectPassword(self):
        userList = self.__database_user.select_Users()
        adminList = self.__database_admin.select_Administrators()
        for user in userList:
            self.data[user.get_username()] = user.get_password()
        for admin in adminList:
            self.data[admin.get_username()] = admin.get_password()

    def accountsSelectType(self):
        userList = self.__database_user.select_Users()
        adminList = self.__database_admin.select_Administrators()
        for user in userList:
            self.data[user.get_username()] = "普通用户"
        for admin in adminList:
            self.data[admin.get_username()] = admin.get_type()

    def accountInsert(self, accountName: str, accountPassword: str, accountType: str):
        if accountType == "普通用户":
            self.__database_user.insert_User(User(accountName, accountPassword))
        else:
            self.__database_admin.insert_Administrator(Administrator(accountName, accountPassword, accountType))
        self.state = "成功"
        self.information = accountType + accountName + "添加成功"

    def accountUpdatePassword(self, accountName: str, newPassword: str, accountType: str):
        if accountType == "普通用户":
            self.__database_user.update_UserSecret_By_UserName(accountName, newPassword)
        else:
            self.__database_admin.update_AdministratorSecret_By_AdministratorName(accountName, newPassword)
        self.state = "成功"
        self.information = accountType + accountName + "密码修改成功"

    def adminUpdateType(self, adminName: str, newType: str):
        self.__database_admin.update_AdministratorType_By_AdministratorName(adminName, newType)
        self.state = "成功"
        self.information = adminName + "已变更为" + newType

    def accountDelete(self, accountName: str, accountType: str):
        if accountType == "普通用户":
            self.__database_user.delete_User_By_UserName(accountName)
        else:
            self.__database_admin.delete_Administrator_By_AdministratorName(accountName)
        self.state = "成功"
        self.information = accountType + accountName + "删除成功"

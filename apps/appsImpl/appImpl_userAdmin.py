from database import Database_user, Database_administrator
from pojo import User


class AppImplUserAdmin:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.data = {}              # 数据传输字典
        self.__database_user = Database_user()
        self.__database_admin = Database_administrator()

    def usersSelectPassword(self):
        usersList = self.__database_user.select_Users()
        for user in usersList:
            self.data[user.get_username()] = user.get_password()
            # self.data[user.get_username() + "_flag"] = str(user.get_flag())

    def usersSelectFlag(self):
        usersList = self.__database_user.select_Users()
        for user in usersList:
            self.data[user.get_username()] = str(user.get_flag())

    def userInsert(self, userName: str, userPassword: str, userFlag: bool = False):
        usersList = self.__database_user.select_Users()
        adminsList = self.__database_admin.select_Administrators()
        allUsersNameList = []
        for user in usersList:
            allUsersNameList.append(user.get_username())
        for admin in adminsList:
            allUsersNameList.append(admin.get_username())
        if userName in allUsersNameList:
            self.state = "失败"
            self.information = "已存在此用户，无法注册"
        else:
            userInsert = User(userName, userPassword, userFlag)
            self.__database_user.insert_User(userInsert)
            self.state = "成功"
            self.information = "注册成功"

    def userUpdatePassword(self, userName, newPassword):
        self.__database_user.update_UserSecret_By_UserName(userName, newPassword)
        self.state = "成功"
        self.information = "密码修改成功"

    def userUpdateForbidden(self, userName, newFlag):
        self.__database_user.update_UserForbidden_By_UserName(userName, newFlag)
        self.state = "成功"
        self.information = "封禁标志修改成功"

    def userDelete(self, userName):
        self.__database_user.delete_User_By_UserName(userName)
        self.state = "成功"
        self.information = "用户删除成功"

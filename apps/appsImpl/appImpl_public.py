from database import Database_user, Database_administrator


class AppImplPublic:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.usertype = None        # 用户类型
        self.__database_user = Database_user()
        self.__database_admin = Database_administrator()

    def login(self, username: str, password: str):
        # 利用try-except语句区分普通用户与管理员和不存在的用户
        user = None
        admin = None
        try:
            user = self.__database_user.select_User_By_UserName(username)
        except Exception:
            try:
                admin = self.__database_admin.select_Administrator_By_AdministratorName(username)
            except Exception:
                self.state = "失败"
                self.information = "用户不存在"
                return
        # 若为普通用户
        if user is not None:
            if user.get_flag():
                self.state = "失败"
                self.information = "账户已被锁定"
                return
            if user.get_password() == password:
                self.state = "成功"
                self.information = "登陆成功"
                self.usertype = "普通用户"
                if user.get_surplus() != 3:
                    self.__database_user.update_UserSurplus_By_UserName(username, 3)
                return
            else:
                self.state = "失败"
                if user.get_surplus() == 0:
                    self.information = "密码错误，账户已被锁定"
                    self.__database_user.update_UserForbidden_By_UserName(user.get_username(), True)
                    return
                self.information = "密码错误，登陆失败。您还剩{}次输入错误机会".format(user.get_surplus() - 1)
                self.__database_user.update_UserSurplus_By_UserName(user.get_username(), user.get_surplus() - 1)
        # 若为管理员用户
        if admin is not None:
            if admin.get_password() == password:
                self.state = "成功"
                self.information = "登陆成功"
                self.usertype = admin.get_type()
                return
            else:
                self.state = "失败"
                self.information = "密码错误，登陆失败"
                return


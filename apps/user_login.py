from database import Database_root


class user_login:
    def __init__(self):
        # 登陆设置
        self.list = [{"account": ["password", 3]}]  # 账户列表
        self.timeOut = 3  # 用户的登陆的错误上限
        self.root_timeOut = 1000  # 管理员的登陆错误上限
        # 便捷登陆设置：用于程序员快速测试页面功能
        self.list.append({"a": ["a", 100]})
        # 数据库的设置
        self.database = Database_root()
        self.user_init()

    # 数据库用户表的接口函数：账户列表信息初始化
    def user_init(self):
        # 管理员信息初始化
        administrator_data = self.database.select("administrator_table")
        for i in range(len(administrator_data)):
            self.list.append({administrator_data[i][0]: [administrator_data[i][1], self.root_timeOut]})
        # 用户信息初始化
        user_data = self.database.select("user_table")
        for i in range(len(user_data)):
            # 若用户被封禁,则将其登陆错误上限设置为0,否则设置为timeOut
            if user_data[i][2]:
                self.list.append({user_data[i][0]: [user_data[i][1], 0]})
            else:
                self.list.append({user_data[i][0]: [user_data[i][1], self.timeOut]})

    # 数据库用户表的接口函数：注册插入新账户信息
    def user_insert(self, user_name, user_secret):
        self.database.insert("user_table", [user_name, user_secret, False])

    # 数据库用户表的接口函数：更新用户表信息(封禁账户)
    def user_update(self, account):
        self.database.update("user_table", [account, "forbidden", True])

    def login(self, account, password):
        # 遍历整个账户列表查询该账户
        while self.list:
            temp = self.list.pop()
            # 若查到该账户
            if str(account) in temp:
                # 若账户已被锁定
                if temp[str(account)][1] == 0:
                    # QMessageBox.warning(self, "注意", "错误3次，账户已被锁定！")
                    return "失败", "账户已被锁定"
                # 若账户未被锁定
                else:
                    # 若密码正确
                    if temp[str(account)][0] == str(password):
                        # # 通过数据库实现记住账户功能
                        # self.user_remembered_reset(str(account), str(password),
                        #                            self.checkBox_rememberPassword.isChecked())
                        # QMessageBox.information(self, "提示", "登陆成功")
                        return "成功", "登陆成功"
                    # 若密码错误***********利用数据库实现错误机会，目前未实现
                    else:
                        return "失败", "密码错误，登陆失败"
            # 暂时若未查到该用户
            else:
                continue
        # 若未查到
        return "失败", "用户不存在"

    def register(self, account, password):
        try:
            self.user_insert(str(account), str(password))  # 数据库用户表添加temp用户
            return "成功", "注册成功"
        except Exception:
            print(Exception)
            return "失败", "注册失败"


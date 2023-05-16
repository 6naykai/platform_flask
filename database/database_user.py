from database.database_interface import openGauss
from pojo import User


# 普通用户表接口类: user_table
class Database_user:
    def __init__(self):
        self.__database_interface = openGauss()

    def select_User_By_UserName(self, userName: str) -> User:
        """
        对普通用户表进行根据用户名查询用户的操作
        :param userName: str型(用户名)
        :return: User对象(用户)
        """
        sql = "select user_name,user_secret, user_forbidden, user_surplus" + " " + \
              "from user_table" + " " + \
              "where user_name='{}';"
        data = self.__database_interface.getData(sql.format(userName))
        return User(data[0][0], data[0][1], data[0][2], data[0][3])

    def select_Users(self) -> list:
        """
        对普通用户表进行查询整个表的操作
        :return: list(list中的内容为User类的对象)
        """
        sql = "select * from user_table;"
        data = self.__database_interface.getData(sql)
        users_list = []
        for i in range(len(data)):
            users_list.append(User(data[i][0], data[i][1], data[i][2], data[i][3]))
        return users_list

    def insert_User(self, insertUser: User) -> None:
        """
        对普通用户表进行插入1个普通用户的操作
        :param insertUser: User对象(待插入的用户)
        :return: void
        """
        sql = "insert into user_table (user_name,user_secret,user_forbidden,user_surplus) values ('{}','{}','{}','{}');"
        self.__database_interface.ExecuSQL(sql.format(insertUser.get_username(), insertUser.get_password(),
                                                      insertUser.get_flag(), insertUser.get_surplus()))

    def delete_User_By_UserName(self, userName: str) -> None:
        """
        对普通用户表进行根据用户名删除用户的操作
        :param userName: str(待删除用户的用户名)
        :return: void
        """
        sql = "delete from user_table where user_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(userName))

    def update_UserSecret_By_UserName(self, userName: str, newPassword: str) -> None:
        """
        对普通用户表进行根据用户名修改密码的操作
        :param userName: str(待更新密码的用户用户名)
        :param newPassword: str(变更的新密码)
        :return: void
        """
        sql = "update user_table set user_secret='{}' where user_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newPassword, userName))

    def update_UserForbidden_By_UserName(self, userName: str, newFlag: bool) -> None:
        """
        对普通用户表进行根据用户名修改用户封禁标志的操作
        :param userName: str(待更新封禁标志的用户用户名)
        :param newFlag: bool(变更的新标志)
        :return: void
        """
        sql = "update user_table set user_forbidden='{}' where user_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newFlag, userName))

    def update_UserSurplus_By_UserName(self, userName: str, newSurplus: int) -> None:
        """
        对普通用户表进行根据用户名修改用户密码错误输入机会的操作
        :param userName: str(待更新密码错误输入机会的用户用户名)
        :param newSurplus: int(变更的新密码错误输入机会)
        :return: void
        """
        sql = "update user_table set user_surplus='{}' where user_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newSurplus, userName))
        pass


if __name__ == '__main__':
    test = Database_user()
    user = test.select_User_By_UserName("root1")
    print(user.ToString())


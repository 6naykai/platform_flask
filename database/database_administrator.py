from .database_interface import openGauss
from pojo import Administrator


# 管理员表接口类: administrator_table
class Database_administrator:
    def __init__(self):
        self.__database_interface = openGauss()

    def select_Administrator_By_AdministratorName(self, administratorName: str) -> Administrator:
        """
        对管理员用户表进行根据管理员用户名进行查询管理员的操作
        :param administratorName: str(管理员用户名)
        :return: Administrator对象(管理员)
        """
        sql = "select administrator_name,administrator_secret, administrator_type" + " " + \
              "from administrator_table" + " " + \
              "where administrator_name='{}';"
        data = self.__database_interface.getData(sql.format(administratorName))
        return Administrator(data[0][0], data[0][1], data[0][2])

    def select_Administrators(self) -> list:
        """
        对管理员用户表进行查询整个表的操作
        :return: list(list中的内容为Administrator类的对象)
        """
        sql = "select * from administrator_table;"
        data = self.__database_interface.getData(sql)
        administrators_list = []
        for i in range(len(data)):
            administrators_list.append(Administrator(data[i][0], data[i][1], data[i][2]))
        return administrators_list

    def insert_Administrator(self, insertAdministrator: Administrator) -> None:
        """
        对管理员用户表进行插入1个管理员的操作
        :param insertAdministrator: Administrator对象(待插入的管理员)
        :return: void
        """
        sql = "insert into administrator_table (administrator_name,administrator_secret,administrator_type) values (" \
              "'{}','{}','{}'); "
        self.__database_interface.ExecuSQL(sql.format(insertAdministrator.get_username(),
                                                      insertAdministrator.get_password(),
                                                      insertAdministrator.get_type()))

    def delete_Administrator_By_AdministratorName(self, administratorName: str) -> None:
        """
        对管理员用户表进行根据管理员用户名删除管理员的操作
        :param administratorName: str(待删除管理员的用户名)
        :return: void
        """
        sql = "delete from administrator_table where administrator_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(administratorName))

    def update_AdministratorSecret_By_AdministratorName(self, administratorName: str, newPassword: str) -> None:
        """
        对管理员用户表进行根据管理员用户名修改管理员用户密码的操作
        :param administratorName: str(待更新密码的管理员用户名)
        :param newPassword: str(变更的新密码)
        :return: void
        """
        sql = "update administrator_table set administrator_secret='{}' where administrator_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newPassword, administratorName))

    def update_AdministratorType_By_AdministratorName(self, administratorName: str, newType: str) -> None:
        """
        对管理员用户表进行根据管理员用户名修改管理员类型的操作
        :param administratorName: str(待更新管理员类型的管理员用户名)
        :param newType: str(变更的新管理员类型)
        :return: void
        """
        sql = "update administrator_table set administrator_type='{}' where administrator_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newType, administratorName))

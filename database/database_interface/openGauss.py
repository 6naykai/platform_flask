import psycopg2
from settings import DATABASE, USER, PASSWORD, URL, openGauss_PORT


# openGauss数据库接口类
class openGauss:
    def __init__(self):
        self.Database = DATABASE
        self.User = USER
        self.Password = PASSWORD
        self.URL = URL
        self.openGauss_PORT = openGauss_PORT

    # 建立连接函数：连接数据库,返回psycopg2的连接对象
    def create_conn(self):
        conn = psycopg2.connect(database=self.Database,
                                user=self.User,
                                password=self.Password,
                                host=self.URL,
                                port=str(self.openGauss_PORT))
        return conn

    # sql语句执行函数(无返回值),argv:需要执行的sql语句
    def ExecuSQL(self, argv):
        conn = self.create_conn()
        cur = conn.cursor()  # 生成游标对象
        cur.execute(argv)  # 执行SQL语句
        conn.commit()
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接

    # sql语句执行函数(有返回值),argv:需要执行的sql语句
    def getData(self, argv):
        conn = self.create_conn()
        cur = conn.cursor()  # 生成游标对象
        cur.execute(argv)  # 执行SQL语句
        data = cur.fetchall()  # 通过fetchall方法获得数据
        cur.close()  # 关闭游标
        conn.close()  # 关闭连接
        return data  # 返回数据列表

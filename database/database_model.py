from .database_interface import openGauss
from pojo import Model


# 模型表接口类: model_table
class Database_model:
    def __init__(self):
        self.__database_interface = openGauss()

    def select_Models(self) -> list:
        """
        对模型表进行查询整个表的操作
        :return: list(list中的内容为Model类的对象)
        """
        sql = "select * from model_table;"
        data = self.__database_interface.getData(sql)
        models_list = []
        for i in range(len(data)):
            models_list.append(Model(data[i][0], data[i][1], data[i][2]))
        return models_list

    def insert_Model(self, insertModel: Model) -> None:
        """
        对模型表进行插入一条模型数据的操作
        :param insertModel: Model对象(待插入的模型)
        :return: void
        """
        sql = "insert into model_table (model_name,model_path,model_type) values ('{}','{}','{}');"
        self.__database_interface.ExecuSQL(sql.format(insertModel.get_modelName(),
                                                      insertModel.get_modelPath(),
                                                      insertModel.get_modelType()))

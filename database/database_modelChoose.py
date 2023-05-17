from .database_interface import openGauss
from pojo import ModelChoose


# AI功能板块表接口类: model_Choose_table
class Database_modelChoose:
    def __init__(self):
        self.__database_interface = openGauss()

    def update_ModelChooseModel_By_ModelChooseName(self, newModelChoose: ModelChoose) -> None:
        """
        对AI功能板块表进行根据AI功能板块功能名称修改AI功能板块选用模型对应的模型名称的操作
        :param newModelChoose: 新构建的ModelChoose对象 (这是一种新的方式,可以完美的利用好pojo层)
        :return:
        """
        sql = """update "modelChoose_table" set "modelChoose_model"='{}' where "modelChoose_name"='{}';"""
        self.__database_interface.ExecuSQL(sql.format(newModelChoose.get_modelChooseName(),
                                                      newModelChoose.get_modelChooseModel().get_modelName()))

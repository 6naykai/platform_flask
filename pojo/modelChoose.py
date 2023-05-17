from pojo import Model


class ModelChoose:
    def __init__(self, modelChooseName: str, modelChooseModel: Model):
        self.__modelChooseName = modelChooseName
        self.__modelChooseModel = modelChooseModel

    def get_modelChooseName(self) -> str:
        return self.__modelChooseName

    def set_modelChooseName(self, modelChooseName: str) -> None:
        self.__modelChooseName = modelChooseName

    def get_modelChooseModel(self) -> Model:
        return self.__modelChooseModel

    def set_modelChooseModel(self, modelChooseModel: Model) -> None:
        self.__modelChooseModel = modelChooseModel


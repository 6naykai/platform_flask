class Model:
    def __init__(self, modelName, modelPath, modelType):
        self.__modelName = modelName
        self.__modelPath = modelPath
        self.__modelType = modelType

    def get_modelName(self):
        return self.__modelName

    def set_modelName(self, modelName):
        self.__modelName = modelName

    def get_modelPath(self):
        return self.__modelPath

    def set_modelPath(self, modelPath):
        self.__modelPath = modelPath

    def get_modelType(self):
        return self.__modelType

    def set_modelType(self, modelType):
        self.__modelType = modelType

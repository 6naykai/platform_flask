class Model:
    def __init__(self, modelName, modelPath, modelType):
        self.modelName = modelName
        self.modelPath = modelPath
        self.modelType = modelType

    def get_modelName(self):
        return self.modelName

    def set_modelName(self, modelName):
        self.modelName = modelName

    def get_modelPath(self):
        return self.modelPath

    def set_modelPath(self, modelPath):
        self.modelPath = modelPath

    def get_modelType(self):
        return self.modelType

    def set_modelType(self, modelType):
        self.modelType = modelType

class Game:
    def __init__(self, gameName, gamePath, isAdded):
        self.__gameName = gameName
        self.__gamePath = gamePath
        self.__isAdded = isAdded

    def get_gameName(self):
        return self.__gameName

    def set_gameName(self, musicName):
        self.__gameName = musicName

    def get_gamePath(self):
        return self.__gamePath

    def set_gamePath(self, gamePath):
        self.__gamePath = gamePath

    def get_isAdded(self):
        return self.__isAdded

    def set_isAdded(self, isAdded):
        self.__isAdded = isAdded

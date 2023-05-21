class Music:
    def __init__(self, musicName, musicPath, isAccretion: bool = True):
        self.__musicName = musicName
        self.__musicPath = musicPath
        self.__isAccretion = isAccretion

    def get_musicName(self):
        return self.__musicName

    def set_musicName(self, musicName):
        self.__musicName = musicName

    def get_musicPath(self):
        return self.__musicPath

    def set_musicPath(self, musicPath):
        self.__musicPath = musicPath

    def get_isAccretion(self):
        return self.__isAccretion

    def set_isAccretion(self, isAccretion):
        self.__isAccretion = isAccretion

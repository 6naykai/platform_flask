class Game:
    def __init__(self, gameName, gamePath, isAdded):
        self.gameName = gameName
        self.gamePath = gamePath
        self.isAdded = isAdded

    def get_gameName(self):
        return self.gameName

    def set_gameName(self, musicName):
        self.gameName = musicName

    def get_gamePath(self):
        return self.gamePath

    def set_gamePath(self, gamePath):
        self.gamePath = gamePath

    def get_isAdded(self):
        return self.isAdded

    def set_isAdded(self, isAdded):
        self.isAdded = isAdded

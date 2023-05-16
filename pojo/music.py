class Music:
    def __init__(self, musicName, musicPath, isAccretion):
        self.musicName = musicName
        self.musicPath = musicPath
        self.isAccretion = isAccretion

    def get_musicName(self):
        return self.musicName

    def set_musicName(self, musicName):
        self.musicName = musicName

    def get_musicPath(self):
        return self.musicPath

    def set_musicPath(self, musicPath):
        self.musicPath = musicPath

    def get_isAccretion(self):
        return self.isAccretion

    def set_isAccretion(self, isAccretion):
        self.isAccretion = isAccretion

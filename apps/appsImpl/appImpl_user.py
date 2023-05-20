from database import Database_music, Database_game


class AppImplUser:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.data = {}              # 数据传输字典
        self.__database_music = Database_music()
        self.__database_game = Database_game()

    def musicInit(self):
        musicList = self.__database_music.select_Musics()
        for music in musicList:
            if music.get_isAccretion():
                self.data[music.get_musicName()] = music.get_musicPath()

    def gameInit(self):
        gameList = self.__database_game.select_Games()
        for game in gameList:
            if game.get_isAdded():
                self.data[game.get_gameName()] = game.get_gamePath()

    @staticmethod
    def Download(filepath):
        with open(filepath, 'rb') as f:
            data = f.read(1024)
            while data:
                yield data
                data = f.read(1024)

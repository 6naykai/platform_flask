import os

from database import Database_game
from pojo import Game


class AppImplGameAdmin:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.data = {}              # 数据传输字典
        self.__database_game = Database_game()

    def gamesSelectGamePath(self):
        games = self.__database_game.select_Games()
        for game in games:
            self.data[game.get_gameName()] = game.get_gamePath()

    def gamesSelectIsAdded(self):
        games = self.__database_game.select_Games()
        for game in games:
            self.data[game.get_gameName()] = game.get_isAdded()

    def gameUpdateIsAdded(self, gameName, newIsAdded):
        gameUpdate = self.__database_game.select_Game_By_GameName(gameName)
        self.__database_game.update_IsAdded_By_GameName(gameName, newIsAdded)
        self.state = "成功"
        self.information = "游戏”" + gameName + "“的入库标志修改成功"
        self.data["更新游戏路径"] = gameUpdate.get_gamePath()

    def gameDelete(self, gameName):
        gameDelete = self.__database_game.select_Game_By_GameName(gameName)
        os.remove(gameDelete.get_gamePath())
        self.__database_game.delete_Game_By_GameName(gameName)
        self.state = "成功"
        self.information = "游戏“" + gameName + "”删除成功"
        self.data["删除游戏路径"] = gameDelete.get_gamePath()

    def gameUpload(self, fileName, filePath, fileType):
        if fileType != "exe":
            self.state = "失败"
            self.information = "该文件不是游戏,上传失败"
            os.remove(filePath)
            return
        games = self.__database_game.select_Games()
        for game in games:
            if fileName == game.get_gameName():
                self.state = "失败"
                self.information = "游戏库中已有重名游戏,上传失败"
                os.remove(filePath)
                return
        gameInsert = Game(fileName, filePath)
        self.__database_game.insert_Game(gameInsert)
        self.state = "成功"
        self.information = "游戏“" + fileName + "”上传成功！"

import os
from flask import Response
from util import Result
from apps.appsImpl import AppImplGameAdmin


class AppGameAdmin(AppImplGameAdmin):
    def gamesSelectGamePath_result(self):
        self.gamesSelectGamePath()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def gamesSelectIsAdded_result(self):
        self.gamesSelectIsAdded()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def gameUpdateIsAdded_result(self, gameName, newIsAdded):
        self.gameUpdateIsAdded(gameName, newIsAdded)
        return Result(self.state,
                      self.information).to_Json()

    def gameDelete_result(self, gameName):
        self.gameDelete(gameName)
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def gameUpload_result(self, fileName, filePath, fileType):
        self.gameUpload(fileName, filePath, fileType)
        return Result(self.state,
                      self.information).to_Json()

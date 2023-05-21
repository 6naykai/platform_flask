import os
from flask import Response
from util import Result
from apps.appsImpl import AppImplMusicAdmin


class AppMusicAdmin(AppImplMusicAdmin):
    def musicsSelectMusicPath_result(self):
        self.musicsSelectMusicPath()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def musicsSelectIsAccretion_result(self):
        self.musicsSelectIsAccretion()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def musicUpdateIsAccretion_result(self, musicName, newIsAccretion):
        self.musicUpdateIsAccretion(musicName, newIsAccretion)
        return Result(self.state,
                      self.information).to_Json()

    def musicDelete_result(self, musicName):
        self.musicDelete(musicName)
        return Result(self.state,
                      self.information).to_Json()

    def musicUpload_result(self, fileName, filePath, fileType):
        self.musicUpload(fileName, filePath, fileType)
        return Result(self.state,
                      self.information).to_Json()


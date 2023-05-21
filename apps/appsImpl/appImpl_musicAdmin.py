import os

from database import Database_music
from pojo import Music


class AppImplMusicAdmin:
    def __init__(self):
        self.state = None           # 状态：成功/失败
        self.information = None     # 提示信息
        self.data = {}              # 数据传输字典
        self.__database_music = Database_music()

    def musicsSelectMusicPath(self):
        musics = self.__database_music.select_Musics()
        for music in musics:
            self.data[music.get_musicName()] = music.get_musicPath()

    def musicsSelectIsAccretion(self):
        musics = self.__database_music.select_Musics()
        for music in musics:
            self.data[music.get_musicName()] = music.get_isAccretion()

    def musicUpdateIsAccretion(self, musicName, newIsAccretion):
        self.__database_music.update_IsAccretion_By_MusicName(musicName, newIsAccretion)
        self.state = "成功"
        self.information = "音乐”" + musicName + "“的入库标志修改成功"

    def musicDelete(self, musicName):
        musicDelete = self.__database_music.select_Music_By_MusicName(musicName)
        os.remove(musicDelete.get_musicPath())
        self.__database_music.delete_Music_By_MusicName(musicName)
        self.state = "成功"
        self.information = "音乐“" + musicName + "”删除成功"

    def musicUpload(self, fileName, filePath, fileType):
        if fileType != "mp3":
            self.state = "失败"
            self.information = "该文件不是音乐,上传失败"
            os.remove(filePath)
            return
        musics = self.__database_music.select_Musics()
        for music in musics:
            if fileName == music.get_musicName():
                self.state = "失败"
                self.information = "音乐库中已有重名音乐,上传失败"
                os.remove(filePath)
                return
        musicInsert = Music(fileName, filePath)
        self.__database_music.insert_Music(musicInsert)
        self.state = "成功"
        self.information = "音乐“" + fileName + "”上传成功！"

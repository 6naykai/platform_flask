from .database_interface import openGauss
from pojo import Music


# 音乐表接口类: music_table
class Database_music:
    def __init__(self):
        self.__database_interface = openGauss()

    def select_Musics(self) -> list:
        """
        对音乐表进行查询整个表的操作
        :return: list(list中的内容为Music类的对象)
        """
        sql = "select * from music_table;"
        data = self.__database_interface.getData(sql)
        musics_list = []
        for i in range(len(data)):
            musics_list.append(Music(data[i][0], data[i][1], data[i][2]))
        return musics_list

    def insert_Music(self, insertMusic: Music) -> None:
        """
        对音乐表进行插入一条音乐数据的操作
        :param insertMusic: Music对象(待插入的音乐)
        :return: void
        """
        sql = "insert into music_table (music_name,music_path,is_accretion) values ('{}','{}','{}');"
        self.__database_interface.ExecuSQL(sql.format(insertMusic.get_musicName(),
                                                      insertMusic.get_musicPath(),
                                                      insertMusic.get_isAccretion()))

    def delete_Music_By_MusicName(self, musicName: str) -> None:
        """
        对音乐表进行根据音乐名称删除音乐数据的操作
        :param musicName: Music对象(待删除音乐的音乐名称)
        :return: void
        """
        sql = "delete from music_table where music_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(musicName))

    def update_IsAccretion_By_MusicName(self, musicName: str, newIsAccretion: bool) -> None:
        """
        对音乐表进行根据音乐名称修改音乐入库标记的操作
        :param musicName: str(待更新入库标记的音乐音乐名称)
        :param newIsAccretion: bool(变更的新入库标记)
        :return:
        """
        sql = "update music_table set is_accretion='{}' where music_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newIsAccretion, musicName))

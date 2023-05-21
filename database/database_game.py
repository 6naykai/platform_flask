from .database_interface import openGauss
from pojo import Game


# 游戏表接口类: game_table
class Database_game:
    def __init__(self):
        self.__database_interface = openGauss()

    def select_Game_By_GameName(self, gameName: str) -> Game:
        """
        对游戏表进行根据游戏名查询游戏的操作
        :param gameName: str型(游戏名)
        :return: Game对象(游戏)
        """
        sql = "select game_name,game_path, is_added" + " " + \
              "from game_table" + " " + \
              "where game_name='{}';"
        data = self.__database_interface.getData(sql.format(gameName))
        return Game(data[0][0], data[0][1], data[0][2])

    def select_Games(self) -> list:
        """
        对游戏表进行查询整个表的操作
        :return: list(list中的内容为Game类的对象)
        """
        sql = "select * from game_table;"
        data = self.__database_interface.getData(sql)
        games_list = []
        for i in range(len(data)):
            games_list.append(Game(data[i][0], data[i][1], data[i][2]))
        return games_list

    def insert_Game(self, insertGame: Game) -> None:
        """
        对游戏表进行插入一条游戏数据的操作
        :param insertGame: Game对象(待插入的游戏)
        :return: void
        """
        sql = "insert into game_table (game_name,game_path,is_added) values ('{}','{}','{}');"
        self.__database_interface.ExecuSQL(sql.format(insertGame.get_gameName(),
                                                      insertGame.get_gamePath(),
                                                      insertGame.get_isAdded()))

    def delete_Game_By_GameName(self, gameName: str) -> None:
        """
        对游戏表进行根据游戏名称删除游戏数据的操作
        :param gameName: Game对象(待删除游戏的游戏名称)
        :return: void
        """
        sql = "delete from game_table where game_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(gameName))

    def update_IsAdded_By_GameName(self, gameName: str, newIsAdded: bool) -> None:
        """
        对游戏表进行根据游戏名称修改游戏入库标记的操作
        :param gameName: str(待更新入库标记的游戏游戏名称)
        :param newIsAdded: bool(变更的新入库标记)
        :return: void
        """
        sql = "update game_table set is_added='{}' where game_name='{}';"
        self.__database_interface.ExecuSQL(sql.format(newIsAdded, gameName))

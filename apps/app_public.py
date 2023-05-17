from util import Result
from apps.appsImpl import AppImplPublic


class AppPublic(AppImplPublic):
    def login_result(self, username: str, password: str):
        self.login(username, password)
        data_dict = {"用户类型": self.usertype}
        return Result(self.state,
                      self.information,
                      data_dict).to_Json()


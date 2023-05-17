from apps.appsImpl import user_loginImpl
from util import Result


class user_login(user_loginImpl):
    def login_result(self, username, password):
        state, tishi = self.login(username, password)
        return Result(state, tishi).to_Json()

    def register_result(self, username, password):
        state, tishi = self.login(username, password)
        return Result(state, tishi).to_Json()

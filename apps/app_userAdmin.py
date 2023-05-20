import os

from flask import Response
from util import Result
from apps.appsImpl import AppImplUserAdmin


class AppUserAdmin(AppImplUserAdmin):
    def usersSelectPassword_result(self):
        self.usersSelectPassword()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def usersSelectFlag_result(self):
        self.usersSelectFlag()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def userInsert_result(self, userName: str, userPassword: str, userFlag: bool = False):
        self.userInsert(userName, userPassword, userFlag)
        return Result(self.state,
                      self.information).to_Json()

    def userUpdatePassword_result(self, userName, newPassword):
        self.userUpdatePassword(userName, newPassword)
        return Result(self.state,
                      self.information).to_Json()

    def userUpdateForbidden_result(self, userName, newFlag):
        self.userUpdateForbidden(userName, newFlag)
        return Result(self.state,
                      self.information).to_Json()

    def userDelete_result(self, userName):
        self.userDelete(userName)
        return Result(self.state,
                      self.information).to_Json()

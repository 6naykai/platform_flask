import os
from flask import Response
from util import Result
from apps.appsImpl import AppImplRootAdmin


class AppRootAdmin(AppImplRootAdmin):
    def accountsSelectPassword_result(self):
        self.accountsSelectPassword()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def accountsSelectType_result(self):
        self.accountsSelectType()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def accountInsert_result(self, accountName: str, accountPassword: str, accountType: str):
        self.accountInsert(accountName, accountPassword, accountType)
        return Result(self.state,
                      self.information).to_Json()

    def accountUpdatePassword_result(self, accountName: str, newPassword: str, accountType: str):
        self.accountUpdatePassword(accountName, newPassword, accountType)
        return Result(self.state,
                      self.information).to_Json()

    def adminUpdateType_result(self, adminName: str, newType: str):
        self.adminUpdateType(adminName, newType)
        return Result(self.state,
                      self.information).to_Json()

    def accountDelete_result(self, accountName: str, accountType: str):
        self.accountDelete(accountName, accountType)
        return Result(self.state,
                      self.information).to_Json()

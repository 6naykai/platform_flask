import os

from flask import Response
from util import Result
from apps.appsImpl import AppImplUser


class AppUser(AppImplUser):
    def musicInit_result(self):
        self.musicInit()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def musicDownload(self, filepath):
        return Response(self.Download(filepath), mimetype="audio/mpeg3")

    def gameInit_result(self):
        self.gameInit()
        return Result(self.state,
                      self.information,
                      self.data).to_Json()

    def gameDownload(self, filepath):
        response = Response(self.Download(filepath), mimetype="application/octet-stream")
        fsize = os.path.getsize(filepath)
        response.headers['Content-Length'] = fsize
        return response

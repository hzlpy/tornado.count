# coding:utf-8

import tornado
from tornado import gen
from tornado.web import HTTPError

from handler.api.base import BaseHandler
#from data.collections import User


class ProfileHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        pass

    def put(self):
        pass

    # TODO：对昵称和描述进行限制
    @staticmethod
    def vaildate_nickname(nickname):
        pass

    @staticmethod
    def vaildate_description(description):
        pass


class AvatarUploadHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        pass

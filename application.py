# coding:utf-8

import os

from url import urls
import tornado.web
import config
import torndb

from handler.api.base import APINotFoundHandler
from handler.api.user.logopt import LoginHandler, LogoutHandler
from handler.api.user.register import RegisterHandler, SchoolsHandler
from tornado.options import options

class Application(tornado.web.Application):
    def __init__(self):
        handlers = urls
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=True,
            allow_remote_access=True,
        )
        conn = torndb.Connection(config.DB_HOST + ":" + str(config.DB_PORT),
                                 config.DB_NAME, user=config.DB_USER, password=config.DB_PWD)
        self.db = conn

        tornado.web.Application.__init__(self, handlers, **settings)

# coding:utf-8

from handler.api.base import APINotFoundHandler
from handler.api.user.logopt import LoginHandler, LogoutHandler
#from handler.api.user.profile import ProfileHandler, AvatarUploadHandler
from handler.api.user.register import RegisterHandler, SchoolsHandler
from tornado.options import options

urls = [
    (r"/api/user/register", RegisterHandler),
    (r"/api/user/login", LoginHandler),
    (r"/api/user/logout", LogoutHandler)
]

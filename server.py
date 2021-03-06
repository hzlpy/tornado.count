#!/usr/bin/env python
# coding:utf-8

from tornado import ioloop
import tornado.netutil
import tornado.options
import tornado.httpserver
from tornado.options import define, options, parse_command_line
# from motorengine import connect


import config

define("port", group='Webserver', type=int,
       default=80, help="Run on the given port")
define("subpath", group='Webserver', type=str,
       default="", help="Url subpath (such as /nebula)")
define('unix_socket', group='Webserver', default=None,
       help='Path to unix socket to bind')


def main():
    options.logging = None
    parse_command_line()
    options.subpath = options.subpath.strip('/')
    if options.subpath:
        options.subpath = '/' + options.subpath

    # Connect to mongodb
    io_loop = ioloop.IOLoop.instance()
    # conn = torndb.Connection(config.DB_HOST + ":" + str(config.DB_PORT),
    # config.DB_NAME, user = config.DB_USER, password = config.DB_PWD)

    # self.conn = conn
    # Star application
    from application import Application
    # app.conn=conn

    if options.unix_socket:
        server = tornado.httpserver.HTTPServer(Application())
        socket = tornado.netutil.bind_unix_socket(options.unix_socket, 0o666)
        server.add_socket(socket)
        print('Server is running at %s' % options.unix_socket)
        print('Quit the server with Control-C')

    else:
        http_server = tornado.httpserver.HTTPServer(Application())
        http_server.listen(options.port)
        print('Server is running at http://127.0.0.1:%s%s' %
              (options.port, options.subpath))
        print('Quit the server with Control-C')

    io_loop.start()


if __name__ == "__main__":
    main()

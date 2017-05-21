# coding:utf-8

import tornado
from tornado import gen
from tornado.web import HTTPError

from util.token import token_manager
from handler.api import errors
from handler.api.base import BaseHandler
from data.myredis import myredis
import config

class LoginHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
            # check the key
            key = 'login'
            count = myredis.get(key)
            # get current date
            import time
            today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            sql = "SELECT login_times FROM action WHERE date = '%s'" % today
            if (count):
                count = int(count)
                count = count + 1
                myredis.set(key, count)
                # if count is not less than the limit, update data from Redis to
                # MySQL
                if (count % config.LIMIT == 0):
                    # update count to MySQL
                    if (self.application.db.get(sql)):
                        # update
                        update_time = int(time.time())
                        sql = "UPDATE action SET login_times = %s, update_time = %s WHERE date = '%s'" % (
                            count, update_time, today)
                        print(sql)
                        self.application.db.execute(sql)
                    else:
                        # insert data into MySQL
                        create_time = int(time.time())
                        update_time = create_time
                        register_times = 0
                        login_times = count
                        logout_times = 0
                        sql = "INSERT action(date, register_times, login_times, logout_times, create_time, update_time) VALUES('%s', %s, %s, %s, %s, %s)" % (
                            str(today), register_times, login_times, logout_times, create_time, update_time)
                        print(sql)
                        self.application.db.execute(sql)
            else:
                ret = self.application.db.get(sql)
                if (ret):
                    count = int(ret['login_times'])
                    count = count + 1
                else:
                    count = 1
                myredis.set(key, count)


class LogoutHandler(BaseHandler):
    def get(self):
        # check the key
        key = 'logout'
        count = myredis.get(key)
        # get current date
        import time
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "SELECT logout_times FROM action WHERE date = '%s'" % today
        if (count):
            count = int(count)
            count = count + 1
            myredis.set(key, count)
            # if count is not less than the limit, update data from Redis to
            # MySQL
            if (count % config.LIMIT == 0):
                # update count to MySQL
                if (self.application.db.get(sql)):
                    # update
                    update_time = int(time.time())
                    sql = "UPDATE action SET logout_times = %s, update_time = %s WHERE date = '%s'" % (
                        count, update_time, today)
                    self.application.db.execute(sql)
                else:
                    # insert data into MySQL
                    create_time = int(time.time())
                    update_time = create_time
                    register_times = 0
                    login_times = 0
                    logout_times = count
                    sql = "INSERT action(date, register_times, login_times, logout_times, create_time, update_time) VALUES('%s', %s, %s, %s, %s, %s)" % (
                        str(today), register_times, login_times, logout_times, create_time, update_time)
                    print(sql)
                    self.application.db.execute(sql)
        else:
            ret = self.application.db.get(sql)
            if (ret):
                count = int(ret['logout_times'])
                count = count + 1
            else:
                count = 1
            myredis.set(key, count)

    def data_received(self, chunk):
        pass

    def delete(self):
        pass

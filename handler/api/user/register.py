# coding:utf-8

#from bson import ObjectId
import tornado
from tornado import gen
from tornado.web import HTTPError

from handler.api import errors
from handler.api.base import BaseHandler
from data.myredis import myredis
import config

#from data.collections import User, School
#from util.token import token_manager


class RegisterHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def post(self):
        pass

    # count times of calling RegisterHandler
    def get(self):
        # check the key
        key = 'register'
        count = myredis.get(key)
        # get current date
        import time
        today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        sql = "SELECT register_times FROM action WHERE date = '%s'" % today
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
                    sql = "UPDATE action SET register_times = %s, update_time = %s WHERE date = '%s'" % (
                        count, update_time, today)
                    print(sql)
                    self.application.db.execute(sql)
                else:
                    # insert data into MySQL
                    create_time = int(time.time())
                    update_time = create_time
                    register_times = count
                    login_times = 0
                    logout_times = 0
                    sql = "INSERT action(date, register_times, login_times, logout_times, create_time, update_time) VALUES('%s', %s, %s, %s, %s, %s)" % (
                        str(today), register_times, login_times, logout_times, create_time, update_time)
                    print(sql)
                    self.application.db.execute(sql)
        else:
            ret = self.application.db.get(sql)
            if (ret):
                count = int(ret['register_times'])
                count = count + 1
            else:
                count = 1
            myredis.set('register', count)


class SchoolsHandler(BaseHandler):
    def data_received(self, chunk):
        pass

    def get(self):
        pass

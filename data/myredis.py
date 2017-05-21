# coding:utf-8

import redis
import config

# redis = redis.Redis(
#    connection_pool=
#    redis.ConnectionPool(
#        host=config.REDIS_HOST,
#        port=config.REDIS_PORT,
#        db=0
#    )
#)
#myredis = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)
myredis = redis.Redis(host='localhost', port=6379,
                      password=config.REDIS_PWD, db=0)

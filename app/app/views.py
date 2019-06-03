# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: app
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-03 13:53:35
Last Modified: 2019-06-03 21:31:38
'''

import redis
from app import app


@app.route('/')
def hello():
    return 'hello world'


@app.route('/redis')
def redis_hello():
    r = redis.Redis(host="redis", port=6379)
    return r.info()['rdb_last_save_time']

# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: app
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-03 13:53:35
Last Modified: 2019-06-03 13:54:24
'''


from app import app


@app.route('/')
def hello():
    return 'hello world'

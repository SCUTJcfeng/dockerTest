# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: dockerTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-03 11:45:21
Last Modified: 2019-06-03 21:40:17
'''

import requests


def test_hello():
    assert 'hello world' == requests.get('http://127.0.0.1:5000/').text


def test_redis():
    assert 200 == requests.get('http://127.0.0.1:5000/redis').status_code

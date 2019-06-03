# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: app
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-03 13:52:23
Last Modified: 2019-06-03 13:54:45
'''

from flask import Flask

app = Flask(__name__)
from app import views

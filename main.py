# !/usr/bin/python3.6
# -*- coding:utf-8 -*-
'''
Project: dockerTest
Author: jc feng (jcfeng2013@gmail.com)
File Created: 2019-06-03 11:04:45
Last Modified: 2019-06-03 13:53:16
'''

from app import app


if __name__ == "__main__":
    app.run(host='0.0.0.0')

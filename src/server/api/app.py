# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/23 9:40 PM
 @Author   :TaibiaoGuo
 @FileName :app
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

from flask import Flask

app = Flask(__name__)


if __name__ == '__mainn__':
    app.run(host=app.config["HOST"], port=app.config["PORT"])
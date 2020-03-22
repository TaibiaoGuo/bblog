# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/24 7:50 PM
 @Author   :TaibiaoGuo
 @FileName :ping
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

import pymysql
import socket
import time
import asyncio


class socketping:
    def ping(self, port, host='127.0.0.1'):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        if result == 0:
            return True
        else:
            return False


class pingmysql(socketping):

    def pingMysql(self, port, host):
        """
        通过检查端口来判断服务是否已经启动
        :param port:
        :param host:
        :return: bool
        """
        while self.ping(port=port, host=host) == False:
            print("The Sql Server %s:%d is closed now,waiting 5s...", host, port)
            time.sleep(5)
        print("The Sql Server %s:%d is opened now", host, port)
        return True

    def checkMysql(self, port, host, user, password, dbname):
        """
        通过检查数据库的响应来判断判断Mysql是否可以正常提供服务
        :param port:
        :param host:
        :param user: 数据库用户名
        :param password: 数据库密码
        :param dbname: 数据库名
        :return: bool
        """
        conn = pymysql.connect(host=host, port=port,user=user, password=password, db=dbname)
        status = False
        while status == False:
            try:
                conn.ping()
                return True
            except:
                raise

class pingGeth(socketping):
    def pingGeth(self,port,host):
        return





# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/24 4:45 AM
 @Author   :TaibiaoGuo
 @FileName :osEnv
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

import os


class OSEnv:

    def getOSVariable(self, variable):
        v = os.getenv(str(variable))
        if v == '':
            raise SystemExit("System environment variables are missing！")
        else:
            return v

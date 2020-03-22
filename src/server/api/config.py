# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/24 5:40 AM
 @Author   :TaibiaoGuo
 @FileName :config
 @Github   :https://github.com/TaibiaoGuo
 @Describe : 关于Flask 的 config 介绍操作请参见 https://dormousehole.readthedocs.io/en/latest/config.html

            本服务的配置包含开发和生产环境的配置信息，Config类在启动时，会进行如下初始化操作：
            1、执行Config.__init__()函数；
            2、检查系统环境变量 FLASK_ENV
            2.1、若为空或者 production ，则从./config/production.cgf 文件中载入生产环境配置；
            2.2、若为 development ，则从 ./config/production.cgf 文件中载入开发环境配置；
            3、依次检查环境变量，若有同名的环境变量，则使用系统环境变量替代对应的环境变量；
            4、服务启动，打印日志信息。
'''

from utils.osEnv import OSEnv

# class Config(object):
#     # DB base
#     JSON_AS_ASCII = False  # support chinese
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#
#     # Flask base
#     HOST = "0.0.0.0"
#     PORT = '5000'
#
#     def __init__(self):
#         if OSEnv.getOSVariable('FLASK_ENV') == 'development':
#             # Flask
#             SECRET_KEY = "bblog"
#
#             # DB
#             SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'
#
#             # ETH
#             ROOT_PRIVATE_KEY = '622C5B7B7BC8B728E07F6E04A9FDC5F46EC6273574E06D86AAA66259B3ECDD95'
#             MAIN_ADDRESS = '0x24736c9d1a4bef7483281f914206ba70be08c099'
#
#         elif OSEnv.getOSVariable('FLASK_ENV') == 'production':




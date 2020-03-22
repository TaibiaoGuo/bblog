# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/24 5:40 AM
 @Author   :TaibiaoGuo
 @FileName :config
 @Github   :https://github.com/TaibiaoGuo
 @Describe : 关于Flask 的 config 介绍操作请参见 https://dormousehole.readthedocs.io/en/latest/config.html
'''

from utils.osEnv import OSEnv
import os
from appdirs import AppDirs


class CConfig(object):
    # DB base
    JSON_AS_ASCII = False  # support chinese
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask base
    HOST = "0.0.0.0"
    PORT = '5000'
    SQLALCHEMY_DATABASE_URI = ""
    ROOT_PRIVATE_KEY = ""
    MAIN_ADDRESS = ""
    provider = ""
    curr_dir=""

    def __init__(self):
        # Flask
        self.SECRET_KEY = "bblog"

        # DB
        self.SQLALCHEMY_DATABASE_URI = 'sqlite:///sqlite.db'

        # ETH
        self.ROOT_PRIVATE_KEY = OSEnv.getOSVariable(self,'PRIVATE_KEY')
        self.MAIN_ADDRESS = OSEnv.getOSVariable(self,'MAIN_ADDRESS')
        self.provider = OSEnv.getOSVariable(self,'ETH_PROVIDER')
        self.BLOCK_GAS_LIMIT = 6800000
        self.GAS_LIMIT = 6800000
        self.newbie_token = 5000
        self.title_length = 22

        # IPFS
        self.ipfs_host = "bblog-ipfs"
        self.ipfs_port = "5001"

        USER_DATA_DIR = AppDirs("UlordPySdk", "").user_data_dir
        CURR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sols")
        if os.path.isdir(USER_DATA_DIR) is False:
            import shutil
            shutil.copytree(CURR_DIR, USER_DATA_DIR)
        self.CURR_DIR = CURR_DIR
        # for log
        self.curr_dir = os.getcwd()

        self.receipt_watcher_sleep_time = 1

Config = CConfig()
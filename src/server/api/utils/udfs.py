# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/3/23 4:18 AM
 @Author   :TaibiaoGuo
 @FileName :udfs
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

import os
import time
import logging
import ipfsapi

class Udfs(object):
    """udfs helper"""

    def __init__(self, host='114.67.37.2', port='20418'):
        """init a connector"""
        self.connect = ipfsapi.connect(host=host, port=port)
        self.log = logging.getLogger("udfs")

    def config(self, host, port):
        """change connect"""
        self.connect = ipfsapi.connect(host=host, port=port)

    def upload(self, filepath):
        """upload a file to udfs"""
        if os.path.isfile(filepath):
            return self.connect.add(filepath)
        else:
            self.log.error("Not a file:{}".format(filepath))
            return None

    def downloadhash(self, filehash, filepath=None, Debug=False):
        """
        download file from the UDFS according to the udfs hash

        :param filehash: file udfs hash
        :type filehash: str
        :param filepath: the path to save the file
        :type filepath: str
        :param Debug: if Debug print the cost time
        :type Debug: bool
        :return: True or False
        """
        try:
            start = time.time()
            self.connect.get(filehash, filepath=filepath)
            if Debug:
                end = time.time()
                self.log.debug('download {0} cost:{1}'.format(filehash, (end - start)))
                print('download {0} cost:{1}'.format(filehash, (end - start)))
            self.log.info("download {} successfully!".format(filehash))
            return True
        except Exception as e:
            logging.error("download fail:{}".format(e))
            return False


if __name__ == '__main__':
    pass
    # udfshelper = UdfsHelper()
    # udfshelper.upload_file(r'E:\ulord\py-ulord-api\ulordapi\udfs\config.json')
    # with open(r'E:\ulord\py-ulord-api\ulordapi\udfs\config.json', 'r') as target:
    #     udfshelper.upload_file(target)

# !/usr/bin python3
# encoding:utf-8
'''
 @Time     :2020/2/24 5:33 AM
 @Author   :TaibiaoGuo
 @FileName :manage
 @Github   :https://github.com/TaibiaoGuo
 @Describe :
'''

from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import Config

from passlib.apps import custom_app_context as pwd_context
from flask_cors import CORS

 sys.path.append('../')

# initialization
app = Flask(__name__)

# app.config.from_object(DevConfig)
# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bigdata205@45.62.105.143:6003/blockchain_academicrecord?charset=utf8'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['autocommit'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app, session_options={'autocommit': False})

# 跨域问题
cors = CORS(app, resources=r"/*")


def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


db.Model.to_dict = to_dict

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='主键')
    username = db.Column(db.String(66), comment='用户账号')
    password_hash = db.Column(db.String(100), comment='密码')
    timestamp = db.Column(db.String(66), comment='登录时间')
    token = db.Column(db.String(128), index=True)

    @staticmethod
    def hash_password(password):
        return pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Claim(db.Model):
    __tablename__ = 'claim'
    claim_id = db.Column(db.String(66), primary_key=True, comment='商品id')
    udfs = db.Column(db.String(66), comment='UDFS哈希')
    author = db.Column(db.String(66), comment="作者")
    body = db.Column(db.Text, comment='文本内容')
    description = db.Column(db.Text, comment='摘要')
    price = db.Column(db.Integer, comment='价格')
    deposit = db.Column(db.Integer, comment='押金')
    type = db.Column(db.Integer, comment='类型')
    initDate = db.Column(db.Integer, comment='创建日期')
    waive = db.Column(db.BOOLEAN, default=False, comment='是否封禁')
    views = db.Column(db.Integer, default=0, comment='浏览量')
    title = db.Column(db.String(66), default=None, comment='标题')  # rm


class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    claim_id = db.Column(db.String(66), comment='商品id')
    address = db.Column(db.String(128), comment='用户地址')


class UserAddress(db.Model):
    __tablename__ = 'user_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, comment='用户id')
    address = db.Column(db.String(128), comment='用户地址')


class Advertising(db.Model):
    __tablename__ = 'advertising'
    id = db.Column(db.Integer,autoincrement=True)
    claim_id = db.Column(db.String(128), comment='商品id', primary_key=True)
    price = db.Column(db.Integer, comment='价格')
    address = db.Column(db.String(128), comment='用户地址', primary_key=True)
    payment = db.Column(db.BOOLEAN, default=False, comment='是否付钱')
    initDate = db.Column(db.Integer, comment='创建日期')


if __name__ == '__main__':
    db.drop_all()
    print("数据库已删除")
    db.create_all()
    print("数据库已新建")
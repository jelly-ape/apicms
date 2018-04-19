# -*- encoding: utf-8 -*-
from flask_login import UserMixin
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
# 己方库
from apicms.db import admin_collection as table


class User(UserMixin):

    def __init__(self, id, username, password_hash):
        """
        只能被自己类调用
        """
        self.id = str(id)
        self._username = username
        self._password_hash = password_hash

    @property
    def password(self):
        raise AttributeError('password is can not access')

    @password.setter
    def password(self, password):
        """
        设定密码, 会自动进行 Hash 操作

        :param password: 新设定的密码
        """
        password_hash = generate_password_hash(password)
        filter = {'_id': ObjectId(self.id)}
        update = {'$set': {'password_hash': password_hash}}
        result = table.update_one(filter, update)
        if result.acknowledged:
            self._password_hash = password_hash

    def verify_password(self, password):
        """
        验证密码是否正确

        :param password: 待验证的密码
        :return: 返回是否一致
        """
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    @property
    def password_hash(self):
        """
        获取 Hash 的密码
        """
        return self._password_hash

    @property
    def username(self):
        """
        获取用户名
        """
        return self._username

    @staticmethod
    def get(user_id):
        """
        通过 ID 返回 User 对象. 这个函数将在 load_user 中被调用

        :return: 返回 User 对象, 不存在返回 None
        """
        try:
            filter = {'_id': ObjectId(user_id)}
            result = table.find_one(filter)
            username = result['username']
            password_hash = result['password_hash']
            user_id = result['_id']
            return User(user_id, username, password_hash)
        except:
            return None

    @staticmethod
    def add(username, password):
        """
        添加新用户

        :param username: 用户名, 唯一存在
        :param password: 未 hash 的密码
        :return: 添加成功返回 User 对象, 否则返回 None
        """
        # 写数据库
        try:
            password_hash = generate_password_hash(password)
            document = {
                'username': username,
                'password_hash': password_hash,
            }
            result = table.insert_one(document)
            assert result.acknowledged
            user_id = result.inserted_id
        except DuplicateKeyError:  # 已经存在
            raise ValueError('user exists')
        except Exception as e:
            raise ValueError(str(e))

        # 生成对象
        return User(user_id, username, password_hash)

    @staticmethod
    def get_user(username):
        """
        依据 username 获取一个 User 对象

        :return: 返回对应 username 的 User 对象, 不存在返回 None
        """
        try:
            filter = {'username': username}
            result = table.find_one(filter)
            username = result['username']
            password_hash = result['password_hash']
            user_id = result['_id']
            return User(user_id, username, password_hash)
        except:
            return None

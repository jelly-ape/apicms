# -*- encoding: utf-8 -*-
from bson.objectid import ObjectId
from pymongo.errors import DuplicateKeyError
# 己方库
from apicms.db import festival_collection as table


class Festival(object):

    def __init__(self, _id, name, month, day, is_solar):
        """
        标定一个节日

        :param _id: 节日数据在数据库中的 ID
        :param name: 节日名称
        :param month: 月份
        :param day: 日期
        :param is_solar: 是否是阳历
        """
        self._id = str(_id)
        self._name = name
        self._month = int(month)
        self._day = int(day)
        self._is_solar = is_solar

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def month(self):
        return self._month

    @property
    def day(self):
        return self._day

    @property
    def is_solar(self):
        return self._is_solar

    @staticmethod
    def get(_id):
        """
        通过 ID 返回 Festival 对象.

        :return: 返回 Festival 对象, 不存在返回 None
        """
        try:
            filter = {'_id': ObjectId(_id)}
            result = table.find_one(filter)

            _id = result['_id']
            name = result['name']
            month = int(result['month'])
            day = int(result['day'])
            is_solar = result['is_solar']
            return Festival(_id, name, month, day, is_solar)
        except:
            return None

    @staticmethod
    def add(name, month, day, is_solar):
        """
        添加一个节日

        :param name: 节日名称
        :param month: 月份
        :param day: 日期
        :param is_solar: 是否是阳历
        """
        try:
            document = {
                'name': name,
                'month': int(month),
                'day': int(day),
                'is_solar': is_solar,
            }
            result = table.insert_one(document)
            assert result.acknowledged
            _id = result.inserted_id
        except DuplicateKeyError:  # 已经存在
            raise ValueError('festival exists')
        except Exception as e:
            raise ValueError(str(e))

        # 生成对象
            return Festival(_id, name, month, day, is_solar)

    @staticmethod
    def get_festival(name):
        """
        依据 name 获取一个 Festival 对象

        :return: 返回对应 name 的 Festival 对象, 不存在返回 None
        """
        try:
            filter = {'name': name}
            result = table.find_one(filter)

            _id = result['_id']
            name = result['name']
            month = int(result['month'])
            day = int(result['day'])
            is_solar = result['is_solar']
            return Festival(_id, name, month, day, is_solar)
        except:
            return None

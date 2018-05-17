# -*- encoding: utf-8 -*-
from pymongo.errors import DuplicateKeyError
#from db import category_collection as table
#from error import ExistErr, NotExistErr


class Category(object):

    def __init__(self, name, owner, group, crud):
        self.name = name
        self.owner = owner
        self.group = group
        self.crud = crud

    @classmethod
    def add(cls, name, access):
        """
        添加新 category

        :param name: category 的名称, 唯一存在
        :return: 添加成功返回 True, 失败返回 False, 已存在抛出 ExistErr 异常
        """
        document = {'name': name}

        try:
            result = table.insert_one(document)
        except DuplicateKeyError:  # 已经存在
            raise ExistErr

        return result.acknowledged

    def delete(self):
        filter = {'name': self.name}
        result = table.find_one_and_delete(filter)

        if result is None:  # 不存在
            raise NotExistErr

    def update(self, ):
        filter = {'name': self.name}


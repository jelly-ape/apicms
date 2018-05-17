# -*- encoding: utf-8 -*-
import pymongo
from config import Config


client = pymongo.MongoClient(
    Config.MONGO_HOST,
    Config.MONGO_PORT
)
db = client[Config.MONGO_DBNAME]

# 用户
user_collection = db['user']
user_collection.ensure_index('name', unique=True)

# 组
group_collection = db['group']
group_collection.ensure_index('name', unique=True)


# 类别
category_collection = db['category']
category_collection.ensure_index('name', unique=True)

# 条目
item_collection = db['item']
item_collection.ensure_indexes([('name', 'user', 'category')], unique=True)

# -*- encoding: utf-8 -*-
import pymongo
from config import Config


client = pymongo.MongoClient(
    Config.MONGO_HOST,
    Config.MONGO_PORT
)
db = client[Config.MONGO_DBNAME]
# 管理员
admin_collection = db['admin']
admin_collection.ensure_index('username', unique=True)
# 通用节日
festival_collection = db['festival']
festival_collection.ensure_index('name', unique=True)
# 自定义节日
big_day_collection = db['big_day']

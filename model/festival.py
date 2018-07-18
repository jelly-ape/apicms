# -*- encoding: UTF-8 -*-
"""
节日的相关类
"""
from __future__ import unicode_literals, absolute_import

from datetime import date

from model.access import public_festival_access, private_festival_access
from model.mix_date import MixDate


class BaseFestival(object):
    """
    节日的基类
    """

    def __init__(self, name, description, date):
        """
        构造函数

        :param name: 节日名称
        :param description: 节日描述
        :param date: 节日日期 MixData 对象
        """
        self.name = name
        self.description = description
        assert isinstance(date, MixDate), 'date must be MixDate'
        self.date = date

    @property
    def lunar_date(self):
        """
        获取农历日期

        :return: 返回农历的 (年, 月, 日)
        """
        return self.date.lunar_date

    @property
    def solar_date(self):
        """
        获取阳历日历

        :return: 返回阳历的 (年, 月, 日)
        """
        return self.date.solar_date

    def is_today(self):
        """
        判断是不是今天 (北京时间)

        :return: 如果是今天返回 True, 否则返回 False
        """
        today = date.today()
        return (today.year, today.month, today.day) == self.solar_date


class PublicFestival(BaseFestival):
    """
    公共节日, 直接使用基类的功能即可
    """

    def __init__(self, name, description, date):
        """
        构造函数

        :param name: 节日名称
        :param description: 节日描述
        :param date: 节日日期 MixData 对象
        """
        BaseFestival(self, name, description, date)
        self.owner = 'root'  # 拥有者为 root
        self.access = public_festival_access  # owner -> r/w, other -> r


class PrivateFestival(BaseFestival):
    """
    私人节日, 可以记录用户自己的 "纪念日"
    """

    def __init__(self, name, description, date, owner):
        """
        构造函数

        :param name: 节日名称
        :param description: 节日描述
        :param date: 节日日期 MixData 对象
        :param owner: 创建这个节日的拥有者, User 对象
        """
        BaseFestival(self, name, description, date)
        self.owner = owner
        self.access = private_festival_access  # owner -> r/w, other -> NONE

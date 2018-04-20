# -*- encoding: utf-8 -*-
"""
包含农历和阳历的日历工具
"""
from copy import copy
from lunardate import LunarDate
from datetime import date as SolarDate


class MixDate(object):
    """
    包含农历和阳历的日历
    """

    def __init__(self, month, day, is_solar=True):
        """
        日历不包含年, 因为年是循环的, 只需要给出月和日即可. 支持阳历和阴历

        :param month: 月份
        :param day: 日
        :is_solar: 是否是阳历, 默认为阳历.
        """
        self.month = month
        self.day = day
        self.is_solar = is_solar

        if is_solar:
            today = SolarDate.today()
            year = today.year
            self._solar_date = SolarDate(year, month, day)
            self._lunar_date = LunarDate.fromSolarDate(year, month, day)
        else:
            today = LunarDate.today()
            year = today.year
            self._lunar_date = LunarDate(year, month, day)
            self._solar_date = self._lunar_date.toSolarDate()

    @property
    def solar_date(self):
        """
        获取该日对应的阳历日期, 格式为 (年, 月, 日). 年是当前所在的年份.
        """
        date_tuple = (
            self._solar_date.year,
            self._solar_date.month,
            self._solar_date.day
        )
        return date_tuple

    @property
    def lunar_date(self):
        """
        获取该日对应的阴历日期, 格式为 (年, 月, 日). 年是当前所在的年份.
        """
        date_tuple = (
            self._lunar_date.year,
            self._lunar_date.month,
            self._lunar_date.day
        )
        return date_tuple

    def get(self, year_offset=0):
        """
        依据年份的偏移量给出调整后的 MixDate 对象

        :param year_offset: 年份偏移量
        :return: 返回调整后的 MixDate 对象
        """
        date = copy(self)
        if self.is_solar:
            target_solar_date = SolarDate(
                self._solar_date.year + year_offset,
                self._solar_date.month,
                self._solar_date.day
            )
            target_lunar_date = LunarDate.fromSolarDate(*target_solar_date)
            date._solar_date = target_solar_date
            date._lunar_date = target_lunar_date
        else:
            target_lunar_date = LunarDate(
                self._lunar_date.year + year_offset,
                self._lunar_date.month,
                self._lunar_date.day
            )
            target_solar_date = target_lunar_date.toSolarDate()
            date._solar_date = target_solar_date
            date._lunar_date = target_lunar_date

        return date

    def __str__(self):
        return ('MixDate(month={},day={},is_solar={},solar_date=({},{},{})'
                ',lunar_date=({},{},{}))').format(
            self.month,
            self.day,
            self.is_solar,
            self._solar_date.year,
            self._solar_date.month,
            self._solar_date.day,
            self._lunar_date.year,
            self._lunar_date.month,
            self._lunar_date.day
        )


if __name__ == '__main__':
    d = MixDate(7, 7, False)
    print d
    print d.get(1)
    print d.get(2)
    print d.get(-1)
    print d.solar_date
    print d.lunar_date

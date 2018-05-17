# -*- encoding: utf-8 -*-


class ExistErr(Exception):
    """
    插入时已经存在了
    """
    pass


class NotExistErr(Exception):
    """
    删除, 查找, 修改时不存在
    """
    pass

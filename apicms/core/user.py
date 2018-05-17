# -*- encoding: utf-8 -*-


class User(object):

    def __init__(self, name, group):
        self.name = name
        self.group = group


class Root(User):
    """
    ROOT 用户, 唯一, 全权限
    """

    def __init__(self):
        self.name = 'root'
        self.group = 'root'

# -*- encoding: UTF-8 -*-
"""
权限, 权限对象为 Festival, 每个 Festival 都包含 owner 和 access 两部分.

access 即对 Festival 的 "增删改查" 操作. 将其简化为读/写两类, 分别为:

* 读: 查
* 写: 增删改

其管理对象为 User, 分为两类: owner 和 other. owner 为创建 Festival 的 User.
另外, 还有一类特殊的 User -- root, 其包含所有 Festival 的读/写权限.

权限的读/写表示用 bit 来表达. 从低位到高位, 分别为读, 写. 0 表示不具备该权限,
1 则表示有该权限. 例如:

* owner = 3, 表示 owner 拥有读/写权限
* other = 2, 表示 other 拥有写权限, 但是不具备读权限 (虽然这样不合逻辑)
"""


class Access(object):
    """
    权限对象
    """

    rbit = 0x01  # 读的 bit
    wbit = 0x02  # 写的 bit

    def __init__(self, owner, other):
        assert 0 <= owner <= 3, 'invalid owner access'
        self.owner = owner
        assert 0 <= other <= 3, 'invalid other access'
        self.other = other

    @property
    def other_read(self):
        """
        other 是否有读的权限

        :return: 返回 other 是否有读的权限
        """
        return bool(self.other & self.__class__.rbit)

    @property
    def other_write(self):
        """
        other 是否有写的权限

        :return: 返回 other 是否有写的权限
        """
        return bool(self.other & self.__class__.wbit)

    @property
    def owner_read(self):
        """
        owner 是否有读的权限

        :return: 返回 owner 是否有读的权限
        """
        return bool(self.owner & self.__class__.rbit)

    @property
    def owner_write(self):
        """
        owner 是否有写的权限

        :return: 返回 owner 是否有写的权限
        """
        return bool(self.owner & self.__class__.wbit)


# 公共节日的权限, 作为预设.
#   * owner (root) -> 读/写
#   * other -> 读
public_festival_access = Access(3, 1)

# 私人节日的权限, 作为预设.
#   * owner -> 读/写
#   * other -> 没有权限
private_festival_access = Access(3, 0)

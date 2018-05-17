# -*- encoding: utf-8 -*-
from user import User, Root
from category import Category


class CRUD(object):
    """
    权限包括增删改查, 增是指增加 "子资源" 的权限, 其余操作对象均为自身.
    使用 4 bit 数据来存储, 从高位到低位分别为 "增/查/改/删"
    """

    crud_bits = {
        'c': 0x08,  # create, 增加子资源, 1000
        'r': 0x04,  # retrieve, 查找自身, 0100
        'u': 0x02,  # update, 更改自身, 0010
        'd': 0x01,  # delete, 删除自身, 0001
    }

    def __init__(self, **kwargs):
        """
        权限设置对象. 支持 True/False, 1/0 之类, 会调用 `bool` 来记录

        :param c: 添加 **子资源** 对象的权限, 默认为 0
        :param r: 自身被读取的权限, 默认为 0
        :param u: 修改自身属性的权限, 默认为 0
        :param d: 删除自身的权限, 默认为 0
        :param code: 可直接使用二进制输入, 优先级高于 crud
        """
        if 'code' in kwargs:
            self.__code = kwargs['code']
            print self.__code
        else:
            # 使用
            self.__code = 0x00
            for ch in 'crud':
                if bool(kwargs.get(ch)):
                    self.__code |= self.__class__.crud_bits[ch]

    def __str__(self):
        return 'CRUD({})'.format(bin(self.__code)[2:])

    __repr__ = __str__


class CRUDTuple(object):
    """
    权限元组, 用来记录三元情况, 三元抄自 linux 的文件管理权限方案, 分别为:

    * owner: 创建者/拥有者
    * group: 权限所属的组别名称
    * other: 其他, 即除 owner / group 以外的人
    """

    def __init__(self, owner, group, other):
        """
        不同级别的权限设置对象数据

        :param owner: owner 的 CRUD 权限
        :param group: 设定的 group 的 CRUD 权限
        :param other: 除 owner / group 以外的用户/组别的 CRUD 权限
        """
        assert isinstance(owner, CRUD), 'owner is not CRUD object'
        self.owner = owner
        assert isinstance(group, CRUD), 'group is not CRUD object'
        self.group = group
        assert isinstance(other, CRUD), 'other is not CRUD object'
        self.other = other


class Permission(object):
    """
    判定是否有权限的管理器
    """

    @staticmethod
    def access(resource, user):
        # 判断顺序为 owner > group > other
        if user.name == resource.owner:
            return resource.crud.owner
        elif user.group == resource.group:
            return resource.crud.group
        else:
            return resource.crud.other


if __name__ == '__main__':
    # root 的示例:
    owner = CRUD(c=1, r=1, u=0, d=0)
    group = CRUD(c=1, r=1, u=0, d=0)
    other = CRUD(c=0, r=0, u=0, d=0)
    root_crud = CRUDTuple(owner, group, other)

    resource = Category('test', 'root', 'root', root_crud)

    root = Root()
    ret = Permission.access(resource, root)
    print ret

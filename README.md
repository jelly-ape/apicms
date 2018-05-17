# apicms


## 1. 使用的库

* flask
* flask_RESTful
* flask_login
* gunicorn
* flask_wtf


## 2. API 列表


### 2.1. 获取所有节日


URI: /api/1/festivals

权限：
* GET: 所有人
* POST: 不存在
* UPDATE: 不存在
* DELETE： 不存在

### 2.2. 指定节日

URI: /api/1/festival/{节日名}

权限：
* GET: 所有人
* POST: 管理员
* UPDATE: 管理员
* DELETE： 管理员

### 2.3. 获取所有自定义节日

URI: /api/1/big-days

权限：
* GET: 所有人
* POST: 不存在
* UPDATE: 不存在
* DELETE： 不存在

### 2.4. 指定自定义节日

URI: /api/1/big-day/{节日名}

权限：
* GET: 拥有者
* POST: 拥有者
* UPDATE: 拥有者
* DELETE： 拥有者



1L帖子里说的比较科学，登入/登出对应的服务端资源应该是session，所以相关api应该如下： 

GET /session # 获取会话信息 
POST /session # 创建新的会话（登入） 
PUT /session # 更新会话信息 
DELETE /session # 销毁当前会话（登出） 

而注册对应的资源是user，api如下： 

GET /user/:id # 获取id用户的信息 
POST /user # 创建新的用户（注册） 
PUT /user/:id # 更新id用户的信息 
DELETE /user/:id # 删除id用户（注销）


# 3. 权限设置

每个用户有个用户名 (name, 唯一), 同时可隶属于一个 组别 (group)
资源分为3级, 根目录 > category > item, 每级都存在 增加 (增加子级别资源对象), 删除 (删除自己), 修改 (修改自己), 查找 (查找自己, 获取自身的信息) 四个权限. 权限的设定分为3个对象级别 owner / group / other, 优先级依此降低.
对于 category 和 item 都会记录其创建的 owner 和 group (可设定, 默认为用户所属的 group)

* 根目录 (ower=root, group=groot)

    - 增加 category: (Y/Y/N)
    - 修改自身: (N/N/N)
    - 删除自身: (N/N/N)
    - 查看自身: (Y/Y/N)

* category (owner=root, group=weixin), 修改组别为目标用户组别, 例如 weixin

    - 增加 item: (Y/Y/N)
    - 修改自身: (Y/N/N)
    - 删除自身: (Y/N/N)
    - 查看自身: (Y/Y/N)

* item (owner=user 具体创建的用户, group=weixin, 继承自所属 category)

    - 增加 子级别资源, 不存在, 无意义: (N/N/N)
    - 修改自身: (Y/N/N)
    - 删除自身: (Y/N/N)
    - 查看自身: (Y/N/N)

# apicms


## 1. 使用的库

* flask
* flask-RESTful
* flask-login
* gunicorn


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

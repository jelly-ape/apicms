# -*- encoding: utf-8 -*-
import os
from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
# 己方库
from apicms.admin import admin
from apicms.admin.user import User


app = Flask(__name__)
app.secret_key = os.urandom(24)
csrf = CSRFProtect()
csrf.init_app(app)
login_mgr = LoginManager()
login_mgr.init_app(app)


@login_mgr.user_loader
def load_user(user_id):
    return User.get(user_id)


def init_app():
    app.register_blueprint(admin, url_prefix='/admin')


init_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

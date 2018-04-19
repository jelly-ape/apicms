# -*- encoding: utf-8 -*-
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
# 己方库
from apicms.admin import admin
from apicms.admin.user import User
from apicms.admin.forms import LoginForm


@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.get_user(username)
        if user.verify_password(password):
            login_user(user)
            return redirect(request.args.get('next') or url_for('admin.home'))

    return render_template('login.html', title='login', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('admin.login'))


@admin.route('/home')
@login_required
def home():
    return render_template('admin.html', title='admin')

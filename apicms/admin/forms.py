# -*- encoding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """
    登录表单
    """
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class FestivalForm(FlaskForm):
    """
    公共节日表单
    """
    name = StringField('name', validators=[DataRequired()])
    date = DateField('date', validators=[DataRequired()])

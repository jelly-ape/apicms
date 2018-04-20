# -*- encoding: utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class FestivalForm(FlaskForm):
    """
    公共节日表单
    """
    name = StringField('name', validators=[DataRequired()])
    month = IntegerField('month', validators=[DataRequired()])
    day = IntegerField('day', validators=[DataRequired()])
    is_solar = BooleanField('is_solar', validators=[DataRequired()])

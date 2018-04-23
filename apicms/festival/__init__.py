# -*- encoding: utf-8 -*-
from flask import Blueprint


festival = Blueprint(
    'festival',
    __name__,
    template_folder='templates',
    static_folder='static'
)

from apicms.festival import views

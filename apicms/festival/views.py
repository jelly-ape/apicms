# -*- encoding: utf-8 -*-
from flask import request
from flask import url_for
from flask import redirect
from flask import render_template
from flask_login import login_required
# 己方库
from apicms.festival import festival
from apicms.festival.models import Festival
from apicms.festival.forms import FestivalForm


@festival.route('/add', methods=['POST', 'GET'])
@login_required
def add():
    form = FestivalForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        month = request.form.get('month')
        day = request.form.get('day')
        is_solar = bool(int(request.form.get('is_solar')))
        Festival.add(name, month, day, is_solar)
        return redirect(request.args.get('next') or url_for('festival.home'))

    return render_template('add.html', title='add festival', form=form)


@festival.route('/home')
@login_required
def home():
    return 'LALALA'

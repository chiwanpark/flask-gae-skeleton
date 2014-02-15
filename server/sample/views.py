# -*- coding: utf-8 -*-
from flask import render_template
from server.sample import bp as sample


@sample.route('/')
def index():
    return render_template('index.html')

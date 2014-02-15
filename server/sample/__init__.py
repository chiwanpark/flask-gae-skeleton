# -*- coding: utf-8 -*-
from flask import Blueprint
import logging

bp = Blueprint('sample', __name__, url_prefix='/sample')
logging.info('Blueprint named sample is created.')

import views

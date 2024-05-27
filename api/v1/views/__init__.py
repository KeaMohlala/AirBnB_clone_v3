#!/usr/bin/python3
"""Set up Blueprints"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__)
app_views.url_prefix = '/api/v1'
from.index import *
from.states import *
from.cities import *

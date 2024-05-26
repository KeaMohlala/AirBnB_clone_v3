#!/usr/bin/python3
"""Define routes"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """returns status JSON message for route"""
    return jsonify({"status": "OK"})

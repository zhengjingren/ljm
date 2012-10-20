#coding: utf-8

from flask import Flask
from .extensions import *


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    return app

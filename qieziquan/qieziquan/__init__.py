#coding: utf-8

from flask import Flask
from .extensions import db


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db.init_app(app)
    return app

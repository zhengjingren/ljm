#coding: utf-8

from flask import Flask
from .extensions import db
from .utils import import_object

import os
PROJDIR = os.path.abspath(os.path.dirname(__file__))
ROOTDIR = os.path.split(PROJDIR)[0]

try:
    import qieziquan
except ImportError:
    import site
    site.addsitedir(ROOTDIR)


def create_app(config='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config)
    db.init_app(app)
    register_all(app)
    return app


def register(app, blueprint):
    """blueprint 结构:

        {{blueprint}}/
            __init__.py
            models.py
            views.py

    url prefix统一为blueprint名字。
    """

    url_prefix = '/%s' % blueprint

    views = import_object('qieziquan.%s.views' % blueprint)
    app.register_blueprint(views.app, url_prefix=url_prefix)


def register_all(app):
    """注册所有blueprint"""
    register(app, 'account')

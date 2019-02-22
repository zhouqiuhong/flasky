# -*- coding:utf-8 -*-
"""
@author:zhouqiuhong
@file:config.py
@time:2019/2/21 002115:12
"""
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASKY_MAIL_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = "Flasky Admin <flasky@example.com>"
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@localhost:3306/flaskblog?charset=utf8"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URL") or \
        "mysql+pymysql://root:123456@localhost:3306/flaskblog_test?charset=utf-8"


class ProductConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
                              "mysql+pymysql://root:123456@localhost:3306/flaskblog_product?charset=utf-8"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductConfig,
    "default": DevelopmentConfig,
}


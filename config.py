#-*- coding:UTF-8 -*-

import os
basedir = os.path.abspath(os.path.dirname(__file__))

#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'app.db')
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'you-will-never-guess'

#OPENID_PROVIDERS = [
#        {'name':'Google','url':'https://www.google.com/accounts/o8/id'},
#        {'name':'Yahoo','url':'https://me.yahoo.com'},
#        {'name':'AOL','url':'http://openid.aol.com/<username>'},
#        {'name':'Flickr','url':'http://flickr.com/<username>'},
#        {'name':'MyOpenID','url':'https://www.myopenid.com'}]
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SSL_DISABLE = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <peng.weilin@yahoo.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    KIVIE_CATALOGS = {
               u'内衣':
               {
                   u'黑色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'肤色':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'豹纹':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C'),
                   u'裸灰':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'裸色':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'中国红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'富贵粉':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C','85C'),
                   u'典雅黑':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'幸福红':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'樱花粉':('70A','75A','80A','85A','70B','75B','80B','85B','75C','80C','85C','90C','75D','80D','85D','90D'),
                   u'冰绿':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   u'蜜粉':('70A','75A','80A','85A','70B ','75B','80B','85B','70C','75C','80C'),
                   u'酒红':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   u'黛黑':('70A','75A','80A','85A','70B','75B','80B','85B','70C','75C','80C'),
                   },
               u'内裤':{
                   u'黑色':('M','L','XL'),
                   u'肤色':('M','L','XL'),
                   u'豹纹':('M','L','XL'),
                   u'裸灰':('M','L','XL'),
                   u'裸色':('M','L','XL'),
                   u'中国红':('M','L','XL'),
                   u'富贵粉':('M','L','XL'),
                   u'典雅黑':('M','L','XL','XXL'),
                   u'幸福红':('M','L','XL','XXL'),
                   u'樱花粉':('M','L','XL','XXL'),
                   u'冰绿':('M','L','XL'),
                   u'蜜粉':('M','L','XL'),
                   u'酒红':('M','L','XL'),
                   u'黛黑':('M','L','XL'),
                   u'藕色':('L','XL','XXL'),
                   u'豆绿':('L','XL','XXL'),
                   u'驼灰':('L','XL','XXL'),
                   u'幸运红':('L','XL','XXL'),
                   u'烟青蓝':('L','XL','XXL'),
                   }
               }



    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL')  or \
            'sqlite:///' + os.path.join(basedir,'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URI') or \
            'sqlite:///' + os.path.join(basedir,'data-test.sqlite')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir,'data.sqlite')

    MAIL_SERVER = 'smtp.mail.yahoo.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    @classmethod
    def init_app(cls,app):
        Config.init_app(app)

        """
        # email errors to the administrators
        import logging
        from logging.handlers import SMTPHandler
        credentials = None
        secure = None
        if getattr(cls,'MAIL_USERNAME',None) is not None:
            credentials = (cls.MAIL_USERNAME,cls.MAIL_PASSWORD)
            if getattr(cls,'MAIL_USE_TLS',None):
                secure = ()
        mail_handler = SMTPHandler(
                mailhost=(cls.MAIL_SERVER,cls.MAIL_PORT),
                fromaddr=cls.FLASKY_MAIL_SENDER,
                toaddrs=[cls.FLASKY_ADMIN],
                subject=cls.FLASKY_MAIL_SUBJECT_PREFIX + 'Application Error',
                credentials=credentials,
                secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
        """

class HerokuConfig(ProductionConfig):
    SSL_DISABLE = bool(os.environ.get('SSL_DISABLE')) or True

    @classmethod
    def init_app(cls,app):
        ProductionConfig.init_app(app)

        #handle proxy server headers
        from werkzeug.contrib.fixers import ProxyFix
        app.wsgi_app = ProxyFix(app.wsgi_app)

        # log to stderr
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.WARNING)
        app.logger.addHandler(file_handler)

config = {
        'development':DevelopmentConfig,
        'testing':TestingConfig,
        'production':ProductionConfig,
        'default':DevelopmentConfig,
        'heroku':HerokuConfig,
        }

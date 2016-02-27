# setting maintenance.

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/features.sql'

    SECRET_KEY = "Q!$G!QrGVQ$TRQ!@$QW#GS132877575759322FWE~$"
    SECURITY_PASSWORD_HASH = 'sha256_crypt'
    SECURITY_PASSWORD_SALT = 'asdfasdf2393939393939393'
    SECURITY_REGISTERABLE = True

    WTF_CSRF_CHECK_DEFAULT = False
    WTF_CSRF_ENABLED = False

    SECURITY_POST_LOGIN_VIEW = '/app'


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'features_test',
        'host': '127.0.0.1',
        'port': 27017,
        'connect': False,
    }

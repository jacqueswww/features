# setting maintenance.

class BaseConfig(object):
    DEBUG = False
    TESTING = False

    MONGODB_SETTINGS = {
        'db': 'features',
        'host': '127.0.0.1',
        'port': 27017,
        'connect': False,
    }


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    MONGODB_SETTINGS = {
        'db': 'features_test',
        'host': '127.0.0.1',
        'port': 27017,
        'connect': False,
    }

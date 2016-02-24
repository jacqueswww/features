# setting maintenance.

class BaseConfig(object):
    DEBUG = False
    TESTING = False

    MONGODB_SETTINGS = {}


class ProductionConfig(BaseConfig):
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
    MONGODB_SETTINGS = {

    }

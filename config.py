import datetime
import logging

from common.constant.time_delta import SECONDS_IN_A_DAY
from common.typedef.singleton_instance import Singleton
from common.util.aws_param_store import get_config_from_param_store


class JWTConfig(Singleton):
    def __init__(self):
        self.SECRET_KEY = get_config_from_param_store('/52g/inspection-log/secret-key')
        self.ACCESS_TOKEN_EXPIRES_IN = datetime.timedelta(SECONDS_IN_A_DAY)


class GoogleConfig(Singleton):
    def __init__(self):
        self.GOOGLE_CREDENTIAL = get_config_from_param_store('/52g/inspection-log/google-credential')


class BaseConfig(object):
    # Flask
    ENV = 'development'
    DEFAULT_REGION = 'ap-northeast-2'
    DEBUG = False
    BUNDLE_ERRORS = True
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = JWTConfig.instance().SECRET_KEY
    # Restx
    RESTX_VALIDATE = True
    RESTX_MASK_SWAGGER = False
    # JWT
    JWT_ACCESS_TOKEN_EXPIRES = False
    LOG_LEVEL = logging.DEBUG
    # SQLAlchemy
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# Flask Local Configuration
class LocalConfig(BaseConfig):
    DEBUG = True


# Flask Dev Configuration
class DevConfig(BaseConfig):
    BASE_URL = 'https://inspection-log.52g.studio'


config_by_name = dict(
    local='config.LocalConfig',
    dev='config.DevConfig',
)

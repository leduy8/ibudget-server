import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    SECRET_KEY = "iheartmoney"

    BASIC_AUTH_USERNAME = "admin"
    BASIC_AUTH_PASSWORD = "123456"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/ibudget"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BASE_ITEMS_PER_PAGE = 50

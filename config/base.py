import logging


class BaseConfig:
    LOGGING_LEVEL = logging.INFO

    SECRET_KEY = "iheartmoney"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123456@127.0.0.1/ibudget"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    CATEGORIES_PER_PAGE = 5

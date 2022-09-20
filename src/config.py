from operator import truediv


class BaseConfig():
    SECRET_KEY = "cuchi"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USERNAME="flaskapp.pruebas@gmail.com"
    MAIL_PASSWORD="nxnsdqqummasyuqf"
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    


class DevelopmentConfig(BaseConfig):
    TESTING = True
    DEBUG = True

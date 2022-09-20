from flask import Flask

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")

from services.querys.querys import querys
from services.users.users import users

app.register_blueprint(querys)
app.register_blueprint(users)
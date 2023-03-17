from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
print(app.config)

from . import error_handlers, views, forms, api_views

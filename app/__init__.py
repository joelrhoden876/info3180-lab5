from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from .config import Config
# import flask migrate here
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SECRET_KEY'] = 'some$3cretKey'
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'driver://lab5:UWIMonaLab5@localhost/lab5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
# Instantiate Flask-Migrate library here

migrate = Migrate(app, db) 


from app import views, models

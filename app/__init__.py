from flask import Flask
from .extensions import db, api

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///.db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    api.init_app(app)
    db.init_app(app)
    
    return app
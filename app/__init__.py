from flask import Flask
from .extensions import db, api
from .resources import ns

def create_app():
    app = Flask(__name__)
    
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    api.init_app(app)
    db.init_app(app)
    
    api.add_namespace(ns, path="/api")
    
    return app

# expose app if needed
app = create_app()
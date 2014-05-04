import os
from flask import Flask
from flask.ext.pymongo import PyMongo

mongo = PyMongo()

def create_app():
    config_name = os.environ.get('FLASK_CONFIG', 'development')

    app = Flask(__name__)
    app.config.from_object('config_' + config_name)

    mongo.init_app(app)

    from .hello import hello as hello_blueprint
    app.register_blueprint(hello_blueprint)

    return app

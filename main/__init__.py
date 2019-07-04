##########################################################################
# Name: main
# Purpose: main module which creates the Application instance
#
# Author:     Siva Samudrala
#
# Created:   29/06/2019
# Copyright:   (c) Hoder Solutions Pvt Ltd 2018 - Present
# Licence:   <your licence>
##########################################################################
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from main import config

cors = CORS()
db = SQLAlchemy()
jwt = JWTManager()


def create_app(config_class=config.DefaultConfig):
    """
    Creates the app instance with its own config and other values.
    useful when we need different configs for dev, staging and production
    :param config_class:
    :return: app instance
    """
    app = Flask(__name__)
    app.config.from_object(config.DefaultConfig)

    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    from users.routes import users
    from main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(main)

    return app
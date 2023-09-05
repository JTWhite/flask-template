from flask import Flask
import os 

from .flask_utils import FlaskUtils
from . import config


class FlaskApp(FlaskUtils):

    @classmethod
    def create_app(cls, test_config=None) -> Flask:
        # create and configure the app
        app = Flask(
            __name__,
            instance_relative_config=True,
        )
        app.config.from_object('app.bootstrap.config.Config')

        if test_config is None:
            # load the instance config, if it exists, when not testing
            app.config.from_pyfile('config.py', silent=True)
        else:
            # load the test config if passed in
            app.config.from_mapping(test_config)

        # ensure the instance folder exists
        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass

        # register blueprints
        cls.register_blueprints(app)
    
        return app
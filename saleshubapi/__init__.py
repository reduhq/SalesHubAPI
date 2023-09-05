import os

from flask import Flask

# from saleshubapi.api.api_v1.api import api_bp
from flask_smorest import Api

from saleshubapi.api.api_v1.api import register_blueprints


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        
        API_TITLE = "SalesHubAPI",
        API_VERSION = "v1",
        OPENAPI_VERSION = "3.0.2",
        OPENAPI_URL_PREFIX = "/",
        OPENAPI_SWAGGER_UI_PATH = "/docs",
        OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )

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
    
    api = Api(app)
    register_blueprints(api)
    
    return app
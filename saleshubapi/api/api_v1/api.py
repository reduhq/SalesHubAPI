from flask_smorest import Blueprint
from .endpoints import hello, advertisement

def register_blueprints(api):
    api.register_blueprint(hello.bp, url_prefix="/api/v1/hello")
    api.register_blueprint(advertisement.bp, url_prefix="/api/v1/post")
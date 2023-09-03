from flask import Blueprint
from .endpoints import hello

api_bp = Blueprint("Blueprint", __name__)
api_bp.register_blueprint(hello.bp, url_prefix="/hello")
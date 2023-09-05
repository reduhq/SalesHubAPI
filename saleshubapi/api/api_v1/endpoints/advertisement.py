from flask_smorest import Blueprint

bp = Blueprint("Advertisement", __name__)

@bp.get("/")
def ads():
    return "Returning ads..."
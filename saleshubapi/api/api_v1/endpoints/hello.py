from flask_smorest import Blueprint

bp = Blueprint("Hello", __name__) 

@bp.get("/")
def hola():
    return "hello reduhq"
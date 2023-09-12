from sqlalchemy.future import select

from flask_smorest import Blueprint

from saleshubapi.api.deps import get_connection
from saleshubapi.models.advertisement import Advertisement

bp = Blueprint("Advertisement", __name__)

@bp.get("/")
def ads():
    db = get_connection()
    query = select(Advertisement)
    result = db.execute(query)
    return result.scalars().all()
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from flask_smorest import Blueprint
from flask_smorest import abort

from flask.views import MethodView

from saleshubapi.api.deps import get_connection
from saleshubapi.models.advertisement import Advertisement
from saleshubapi.schemas.advertisement import(
    AdvertisementSchema,
    AdvertisementCreateSchema
)

from datetime import datetime

bp = Blueprint("Advertisement", __name__)

@bp.route("/")
class AdvertisementView(MethodView):
    def __init__(self, db:Session = get_connection()):
        self.db = db
    
    @bp.response(200, AdvertisementSchema(many=True))
    def get(self):
        query = select(Advertisement)
        result = self.db.execute(query)
        return result.scalars().all()
    
    @bp.arguments(AdvertisementCreateSchema)
    @bp.response(200, AdvertisementSchema)
    def post(self, ads_model):
        ads = Advertisement(**ads_model)
        self.db.add(ads)
        self.db.commit()
        self.db.refresh(ads)
        return ads
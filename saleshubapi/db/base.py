# Import all the models, so that Base has them before being
# imported by Alembic
from saleshubapi.db.base_class import Base
from saleshubapi.models.advertisement import Advertisement
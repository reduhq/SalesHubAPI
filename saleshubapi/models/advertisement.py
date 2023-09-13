from sqlalchemy import Column, Integer, String, Date, Boolean, Float
from datetime import date

from saleshubapi.db.base_class import Base

class Advertisement(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(70), nullable=False)
    description = Column(String, nullable=False)
    date = Column(Date, default= date.today, nullable=True )
    establishment = Column(Boolean, nullable=False)
    price = Column(Float, nullable=False)
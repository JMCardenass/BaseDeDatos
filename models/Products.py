from sqlalchemy import Column, Integer, String, Float,

from config.database import Base

class Products(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    price = Column(Float)
    brand = Column(String)
    description = Column(String)
    entry_date = Column(String)
    availability = Column(Integer)
    availability_quantity = Column(Integer)
    
    
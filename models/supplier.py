from sqlalchemy import Column, Integer, String
from config.database import Base
class supplier(Base):
    __tablename__ = 'supplier'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    address = Column(String)
    phone = Column(String)
    email = Column(String)



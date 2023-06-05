from sqlalchemy import Column, Integer, ForeignKey

from config.database import Base
class supplies(Base):
    __tablename__ = 'supplies'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    supplier_id = Column(Integer, ForeignKey('supplier.id'))
    purchase_price = Column(Integer)
    
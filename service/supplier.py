from modesl.supplier import Supplier as ModelSupplier
from schemas.supplier import Supplier as SchemaSupplier

class SupplierService():
    
    def __init__(self, database)->None:
        self.database = database
    
    def get_supplier(self):
        return self.database.query(ModelSupplier).all()
        return result
    
    def create_supplier(self, supplier:SchemaSupplier):
        name = supplier.name
        address = supplier.address
        phone = supplier.phone
        email = supplier.email
        new_supplier = ModelSupplier(name=name, address=address, phone=phone, email=email)
        self.database.add(new_supplier)
        self.database.commit()
        return
    
    def update_supplier(self, id:int, data:SchemaSupplier):
        supplier = self.database.query(ModelSupplier).filter(ModelSupplier.id == id).first()
        supplier.name = data.name
        supplier.address = data.address
        supplier.phone = data.phone
        supplier.email = data.email
        self.database.commit()
        return
    
    def delete_supplier(self, id:int):
        supplier = self.database.query(ModelSupplier).filter(ModelSupplier.id == id).first()
        self.database.delete(supplier)
        self.database.commit()
        return
    
    def get_for_id_supplier(self, id:int):
        return self.database.query(ModelSupplier).filter(ModelSupplier.id == id).first()
        return result

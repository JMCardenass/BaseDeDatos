from modesl.supplies import Supplies as ModelSupplies
from schemas.supplies import Supplies as SchemaSupplies

class SuppliesService():

    def __init__(self, database)->None:
        self.database = database

    def get_supplies(self):
        return self.database.query(ModelSupplies).all()
        return result
    
    def create_supplies(self, supplies:SchemaSupplies):
        name = supplies.name
        price = supplies.price
        brand = supplies.brand
        description = supplies.description
        entry_date = supplies.entry_date
        availability = supplies.availability
        availability_quantity = supplies.availability_quantity
        new_supplies = ModelSupplies(name=name, price=price, brand=brand, description=description, entry_date=entry_date, availability=availability, availability_quantity=availability_quantity)
        self.database.add(new_supplies)
        self.database.commit()
        return
    
    def get_for_id_supplies(self, id:int):
        return self.database.query(ModelSupplies).filter(ModelSupplies.id == id).first()
        return result
    
    def update_supplies(self, id:int, data:SchemaSupplies):
        supplies = self.database.query(ModelSupplies).filter(ModelSupplies.id == id).first()
        supplies.name = data.name
        supplies.price = data.price
        supplies.brand = data.brand
        supplies.description = data.description
        supplies.entry_date = data.entry_date
        supplies.availability = data.availability
        supplies.availability_quantity = data.availability_quantity
        self.database.commit()
        return
    
    def delete_supplies(self, id:int):
        supplies = self.database.query(ModelSupplies).filter(ModelSupplies.id == id).first()
        self.database.delete(supplies)
        self.database.commit()
        return
from models.Products import Products as ProductsModel

class Products:
    def __init__(self,database)-> None:
        self.database = database
        
    def get_products(self):
        return self.database.query(ProductsModel).all()
        return result

    def create_product(self,product:ProductsModel):
        name = product.name
        price = product.price
        brand = product.brand
        description = product.description
        entry_date = product.entry_date
        availability = product.availability
        availability_quantity = product.availability_quantity

    self.database.add(new_product)
    self.database.commit()
    return 
def get_for_id(self,id:int):
    return self.database.query(ProductsModel).filter(ProductsModel.id == id).first()
    return result

def update_product(self,data:ProductsModel):
    product = self.database.query(ProductsModel).filter(ProductsModel.id == data.id).first()
    product.name = data.name
    product.price = data.price
    product.brand = data.brand
    product.description = data.description
    product.entry_date = data.entry_date
    product.availability = data.availability
    product.availability_quantity = data.availability_quantity
    self.database.commit()
    return

def delete_product(self,id:int):
    product = self.database.query(ProductsModel).filter(ProductsModel.id == id).first()
    self.database.delete(product)
    self.database.commit()
    return


    



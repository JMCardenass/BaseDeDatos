from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from service.supplier import SupplierService
from schemas.supplier import Supplier
from config.database import Session 


supplier_router = APIRouter()

@supplier_router.get('/supplier', tags = ['supplier'], status_code=200)
def get_supplier():
    database = Session()
    result = SupplierService(database).get_supplier()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.get('/supplier_for_id', tags = ['supplier'], status_code=200)
def get_supplier_for_id(id:int):
    database = Session()
    result = SupplierService(database).get_for_id_supplier(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplier_router.post('/supplier', tags=['supplier'], status_code= 200)
def create_supplier(supplier:Supplier):
    database = Session()
    SupplierService(database).create_supplier(supplier)
    return JSONResponse(content={"message":"New supplier created", 'status_code': 200})

@supplier_router.put('/supplier{id}', tags=['supplier'])
def update_supplier(id:int,data:Supplier):
    database = Session()
    result = SupplierService(database).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code":400})
    SupplierService(database).update_supplier(id,data)
    return JSONResponse(content={"message":"supplier update succesfull", "status_code":200}, status_code= 200)

@supplier_router.delete('/supplier{id}',tags=['supplier'])
def delete_supplier(id:int):
    database = Session()
    result = SupplierService(database).get_for_id_supplier(id)
    if not result:
        return JSONResponse(content= {"message":"supplier don't found", "status_code": 404})
    SupplierService(database).delete_supplier(id)
    return JSONResponse(content={"message":"supplier delete ", "status_code": 200}, status_code=200)
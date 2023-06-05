from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 
from service.supplies import SuppliesService
from schemas.supplies import Supplies
from config.database import Session


supplies_router = APIRouter()

@supplies_router.get('/supplies', tags = ['supplies'], status_code=200)
def get_supplies():
    database = Session()
    result = SuppliesService(database).get_supplies()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplies_router.get('/supplies_for_id', tags = ['supplies'], status_code=200)
def get_supplies_for_id(id:int):
    database = Session()
    result = SuppliesService(database).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@supplies_router.post('/supplies', tags=['supplies'], status_code= 200)
def create_supplies(supplies:Supplies):
    database = Session()
    SuppliesService(database).create_supplies(supplies)
    return JSONResponse(content={"message":"supplies created", 'status_code': 200})

@supplies_router.put('/supplies{id}', tags=['supplies'])
def update_supplies(id: int, data: Supplies):
    database = Session()
    result = SuppliesService(database).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "supplies not found", "status_code": 400})
    SuppliesService(database).update_supplies(id,data)
    return JSONResponse(content={"message": "supplies updated successfully", "status_code": 200})

@supplies_router.delete('/supplies{id}', tags=['supplies'])
def delete_supplies(id:int):
    database = Session()
    result = SuppliesService(database).get_for_id(id)
    if not result:
        return JSONResponse(content= {"message":"supplies don't found", "status_code": 404})
    SuppliesService(database).delete_supplies(id)
    return JSONResponse(content={"message":"supplies update succesfully","status_code": 200})
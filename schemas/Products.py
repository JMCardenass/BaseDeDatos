from pydantic import BaseModel, Field
from typing import Optional, List

class product(BaseModel):
    id: Optional[int]= Field(None)
    name: str = Field(max_length=50, min_length=3,description="Name of the product")
    price: float = Field(gt=0,description="Price of the product")
    brand: str = Field(max_length=50, min_length=3,description="Brand of the product")
    description: str = Field(max_length=50, min_length=3,description="Description of the product")
    entry_date: str = Field(max_length=50, min_length=3,description="Entry date of the product")
    availability: int = Field(gt=0,description="Availability of the product")
    availability_quantity: int = Field(gt=0,description="Availability quantity of the product")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Coca Cola",
                "price": 1.50,
                "brand": "Coca Cola",
                "description": "Delicioso refresco de cola con coca ",
                "entry_date": "2021-05-01",
                "availability": 1,
                "availability_quantity": 100
            }
        }
        
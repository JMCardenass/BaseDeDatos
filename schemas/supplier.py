from pydantic import BaseModel, Field
from typing import Optional, List

class supplier(BaseModel):
    id: Optional[int]= Field(None)
    name: str = Field(max_length=50, min_length=3,description="Name of the supplier")
    address: str = Field(max_length=50, min_length=3,description="Address of the supplier")
    phone: str = Field(max_length=50, min_length=3,description="Phone of the supplier")
    email: str = Field(max_length=50, min_length=3,description="Email of the supplier")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Coca Cola",
                "address": "Calle 1",
                "phone": "123456789",
                "email": "example@gmail.com"
            }
        }
        
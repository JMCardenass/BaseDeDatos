from pydantic import BaseModel, Field
from typing import Optional, List

class supply(BaseModel):
    id: Optional[int]= Field(None)
    product_id: int = Field(gt=0,description="Id of the product")
    supplier_id: int = Field(gt=0,description="Id of the supplier")

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "product_id": 1,
                "supplier_id": 1
            }
        }
        

from pydantic import BaseModel, Field, model_validator, ConfigDict, EmailStr
from enum import Enum
from datetime import datetime
from typing import List


class OrdersRole:
    STARTED = "started"
    WORKING = "working"
    FINISH = "finish"

class Order(BaseModel):
    id: int = Field()
    telegram_id:str = Field(min_length=3, max_length=100)
    description: str = Field(min_length=3, max_length=250)
    full_name: str = Field(min_length=3, max_length=100)
    role: OrdersRole
    
class UserResponse(Order):
    full_name: str
    role: str
    description: str
    

model_config = ConfigDict(from_attributes=True)
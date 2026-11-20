from pydantic import BaseModel, Field, model_validator, ConfigDict, EmailStr
from enum import Enum
from datetime import datetime
from typing import List

class UserRole(str, Enum):
    CLIENT = "client"
    MASTER = "master"
    ADMIN = "admin"

class User(BaseModel):
    email: EmailStr
    phone: str = Field(min_length=3, max_length=100)
    id: int = Field()
    telegram_id:str = Field(min_length=3, max_length=100)
    full_name: str = Field(min_length=3, max_length=100)
    hashed_password: str = Field(min_length=3, max_length=100)
    role: UserRole 
    
class UserResponse(User):
    id: int
    phone: str
    full_name: str
    role: str
    

model_config = ConfigDict(from_attributes=True)
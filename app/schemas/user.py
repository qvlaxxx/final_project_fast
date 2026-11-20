from datetime import datetime
from enum import Enum

from pydantic import BaseModel, EmailStr

class UserRole(str,Enum):
     CLIENT = "client"
     MASTER = "master"
     ADMIN = "admin"
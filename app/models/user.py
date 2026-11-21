# app/models/user.py
from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class UserRole:
    CLIENT = "client"
    MASTER = "master"
    ADMIN = "admin"
    
class User(Base):
    __tablename__ = "Users"
    email: Mapped[str] = mapped_column(String(20, nullable=True))
    phone: Mapped[str] = mapped_column(String(20, nullable=False))
    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id:Mapped[int | None] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(500), nullable=False)
    role: Mapped[str] = mapped_column(nullable=False,default=UserRole.CLIENT)


    
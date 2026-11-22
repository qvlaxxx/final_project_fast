from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class OrdersRole:
    STARTED = "started"
    WORKING = "working"
    FINISH = "finish"
    OPEN = "open"
    
class Order(Base):
    __tablename__ = "Users"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id:Mapped[int | None] = mapped_column(nullable=True)
    full_name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    role: Mapped[str] = mapped_column(nullable=False,default=OrdersRole.CLIENT)


    
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates # pip install jinja2
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List

from app.database import get_db
from app.models.user import Order, OrderStatus

router = APIRouter(prefix="/orders", tags=["orders"])

templates = Jinja2Templates(directory="templates")

@router.get("/")
def all_orders(request: Request, db:Session = Depends(get_db)):
    all_orders = db.scalars(
        select(Order).where(Order.status == OrderStatus.PENDING)
        ).all
    return templates.TemplateResponse(
        request=request
        name="all_orders.html"
        context={
            "title": "Order"
            "ordres" all_orders
        }
    )

@router.get("/orders{order_id}")
def id_order(request: Request, db:Session = Depends(get_db)):
    Order = db.get(Order,id_order)
    if not Order:
            raise ValueError("не знайдено")
    return templates.TemplateResponse(
    request=request
    name="detail_orders.html"
    context={
        "title": "Order"
        "orders" detail_orders
    }
    return Order
)

@router.get("orders/create")
def order_create(request: Request, db:Session = Depends(get_db)):
    new_order =  Order(**Order.model_dump())
    db.add(new_order)
    db.commit()
    db.refresh(Order)
    return new_order

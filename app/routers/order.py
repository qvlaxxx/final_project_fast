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
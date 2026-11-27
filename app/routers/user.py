from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/register")
def register_get(request: Request):
    return templates.TemplateResponse(request=request, name="register.html")


@router.post("/register")
def register(
    request: Request,
    phone: str = Form(...),
    full_name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    existing = db.scalar(select(User).where(User.phone == phone))
    if existing:
        return templates.TemplateResponse(
            request=request,
            name="register.html",
            context={"error": "Телефон уже занят"},
            status_code=400,
        )

    user = User(phone=phone, full_name=full_name, hashed_password=password)
    db.add(user)
    db.commit()
    return RedirectResponse("/login", status_code=303)


@router.get("/login")
def login_get(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")


@router.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.scalar(select(User).where(User.phone == username))
    if not user or user.hashed_password != password:
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": "Неверный телефон или пароль"},
            status_code=401,
        )
    return RedirectResponse("/orders/", status_code=303)
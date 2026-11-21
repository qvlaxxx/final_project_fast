from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates # pip install jinja2
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from fastapi import Form

from app.database import get_db
from app.models.user import User

router = APIRouter(prefix="/account", tags=["account"])

templates = Jinja2Templates(directory="templates")

@router.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    db = Session()
    user_exists = db.query(User).filter(User.phone == username).first()

    new_user = User(username=username, password=password)
    db.add(new_user)
    db.commit()

    db.close()

@router.get("/register")
def register_get():
    return templates.TemplateResponse(
        request=Request,
        name="register.html"
    )


@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    db = Session()
    user = db.query(User).filter(User.phone == username).first()
    db.close()
    if not user:
        return "User is not registered "
    if password != user.password:
        return "Wrong password "

@router.get("/login")
def register_get():
    return templates.TemplateResponse(
        request=Request,
        name="login.html"
    )

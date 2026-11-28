from fastapi import APIRouter, Depends, HTTPException, status, Request, Form, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates # pip install jinja2
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from pydantic import EmailStr
from urllib.parse import urlencode

from app.database import get_db
from app.models.user import User, UserRole
from app.security import hash_password, check_hashed_password, decode_access_token, create_access_token
from app.routers import templates
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
            context={"error": "такий телефон вже зайнятий"},
            status_code=400,
        )

    user = User(phone=phone, full_name=full_name, hashed_password=password)
    db.add(user)
    db.commit()
    return RedirectResponse("/login", status_code=303)


@router.get("/login")
async def login_get(
    request: Request,
    error: str | None = Query(None),
    notification: str | None = Query(None),
    ):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={
            "error": error,
            "notification": notification
        }
    )

@router.post("/login")
async def login_user(
    request: Request,
    db: Session = Depends(get_db),
    username: str = Form(..., max_length=50),
    password: str = Form(..., max_length=50),
    ):
    user = db.scalar(select(User).where(User.username == username))
    if not user or not check_hashed_password(password, user.hashed_password):
        return templates.TemplateResponse(
            request=request,
            name="login.html",
            context={"error": "Wrong username or password"}
        )
    
    token = create_access_token(user.id)
    params = urlencode({"notification": "Successfully logged in"})
    response = RedirectResponse(url=f"/orders?{params}", status_code=303)
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        max_age=60 * 5
    )
    return response
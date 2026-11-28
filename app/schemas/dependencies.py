from fastapi import Cookie, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User, UserRole
from app.security import decode_access_token


def get_current_user(
    access_token: str | None = Cookie(None),
    db: Session = Depends(get_db),
):
    if not access_token:
        raise HTTPException(
            401,
            detail="не авторизовано"
        )
    user_id =  decode_access_token(access_token)
    if not user_id:\
        raise HTTPException(401,detail="не авторизовано")
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(401,detail="користувача не знайдено")
    
    return user
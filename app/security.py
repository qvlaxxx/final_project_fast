# app/security.py
from datetime import datetime, timedelta, timezone
import bcrypt # blow-fish
import jwt

SECRET_KEY = "secret_key123123123"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 60

def hash_password(raw_password: str):
    hashed_bytes = bcrypt.hashpw(raw_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode("utf-8")

def check_hashed_password(raw_password: str, hashed_password: str):
    return bcrypt.checkpw(raw_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(user_id: int):
    now = datetime.now()
    payload = {
        "sub": str(user_id),
        "iat": now,
        "exp": now + timedelta(minutes=ACCESS_TOKEN_EXPIRE),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('sub', None)
        return int(user_id)
    except jwt.PyJWTError:
        return None

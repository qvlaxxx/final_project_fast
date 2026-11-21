from fastapi import FastAPI, Depends, Request, status, Form, File, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.routers import order

app = FastAPI()

app.include_router(order.router)

@app.get("/healty_check")
def main_healhy_check():
    return {"message": "working"}
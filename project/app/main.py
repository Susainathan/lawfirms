import logging
from fastapi import FastAPI
from . import models
from .database import engine, get_db
from routers import firms


models.Base.metadata.create_all(bind=engine)

log = logging.getLogger("uvicorn")



def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(firms.router)
    return application

app = create_application()

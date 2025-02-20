from fastapi import FastAPI
from app.api.endpoints import router
from app.utils.logging import setup_logging

setup_logging()
app = FastAPI()
app.include_router(router)
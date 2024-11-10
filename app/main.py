from fastapi import FastAPI
from .api import flights

app = FastAPI()

app.include_router(flights.router, prefix="/api")

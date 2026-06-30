from fastapi import FastAPI
from app.api.home import router

app = FastAPI()

app.include_router(router)
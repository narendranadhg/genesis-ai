from fastapi import FastAPI

from app.api.home import router as home_router
from app.api.employee import router as employee_router

app = FastAPI(
    title="Genesis AI",
    version="1.0.0"
)

app.include_router(home_router)
app.include_router(employee_router)
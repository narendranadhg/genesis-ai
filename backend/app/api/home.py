from fastapi import APIRouter, Depends
from app.dependancies import get_company

from app.schemas.profile import ProfileResponse
from app.services.profile_service import get_profile
from app.schemas.employee import Employee

from datetime import datetime

from app.schemas.base_response import BaseResponse

router = APIRouter()


@router.get("/")
def home():
    return {
        "company": "Genesis AI",
        "product": "Atlas"
    }


@router.get("/about")
def about():
    return {
        "founder": "Narendranadh G",
        "vision": "Build Enterprise AI Solutions"
    }


@router.get("/health")
def health():
    return {
        "status": "UP"
    }


@router.get("/profile", response_model=BaseResponse)

def profile():
    profile = get_profile()
    
    response = BaseResponse(
        success=True,
        message="Profile fetched successfully",
        data=profile,
        timestamp=datetime.utcnow()
    )
    return response

@router.get("/company")
def company(info: dict = Depends(get_company)):
   return info 

@router.get("/square/{number}")
def square(number: int):
    return {
        "number": number,
        "square": number * number
    }

@router.get("/search")
def search(name: str):
    return {
        "search_name": name
    }

@router.get("/calculator")
def calculator(a: int, b: int = 0):
    return {
        "sum": a + b
    }   

@router.post("/employee")
def create_employee(employee: Employee):
    return {
        "message": "Employee Created Successfully",
        "employee": employee
    }
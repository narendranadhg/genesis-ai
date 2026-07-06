from fastapi import APIRouter, Depends
from app.dependancies import get_company

from app.services.profile_service import get_profile
from app.schemas.employee import Employee

from app.schemas.base_response import BaseResponse

from app.utils.response import success_response

router = APIRouter()


@router.get("/", response_model=BaseResponse)
def home():
    return success_response(
        message="Home information fetched successfully.",
        data={
            "company": "Genesis AI",
            "product": "Atlas"
        }
    )


@router.get("/about", response_model=BaseResponse)
def about():
    return success_response(
        message="About information fetched successfully.",
        data={
            "founder": "Narendranadh G",
            "vision": "Build Enterprise AI Solutions"
        }
    )


@router.get("/health", response_model=BaseResponse)
def health():
    return success_response(
        message="Health check completed successfully.",
        data={
            "status": "UP"
        }
    )


@router.get("/profile", response_model=BaseResponse)

def profile():
    profile = get_profile()
    
    return success_response(
        message="Profile fetched successfully",
        data=profile
    )


@router.get("/company", response_model=BaseResponse)
def company(info: dict = Depends(get_company)):
   return success_response(
        message="Company information fetched successfully",
        data=info
    )

@router.get("/search", response_model=BaseResponse)
def search(name: str):
    return success_response(
        message="Search completed successfully.",
        data={
            "search_name": name
        }
    )

@router.get("/calculator", response_model=BaseResponse)
def calculator(a: int, b: int = 0):
    return success_response(
        message="Calculation completed successfully.",
        data={
            "sum": a + b
        }
    )

@router.post("/employee" , response_model=BaseResponse)
def create_employee(employee: Employee):
    return success_response(
        message="Employee Created Successfully",
        data=employee
    )


@router.get("/square/{number}", response_model=BaseResponse)
def square(number: int):

    return success_response(
        message="Square calculated successfully.",
        data={
            "number": number,
            "square": number * number
        }
    )
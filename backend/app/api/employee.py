from fastapi import APIRouter

from app.schemas.base_response import BaseResponse
from app.utils.response import success_response

from app.services.employee_service import (
    get_all_employees,
    get_employee,
    search_employees,
    get_employee_address,
)

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.get("/", response_model=BaseResponse)
def get_employees():
    return success_response(
        message="Employees fetched successfully.",
        data=get_all_employees()
    )


@router.get("/{employee_id}", response_model=BaseResponse)
def get_employee_by_id(employee_id: int):
    employee = get_employee(employee_id)

    return success_response(
        message="Employee fetched successfully.",
        data=employee
    )


@router.get("/search/{keyword}", response_model=BaseResponse)
def search(keyword: str):
    return success_response(
        message="Search completed successfully.",
        data=search_employees(keyword)
    )


@router.get("/{employee_id}/address", response_model=BaseResponse)
def employee_address(employee_id: int):
    return success_response(
        message="Address fetched successfully.",
        data=get_employee_address(employee_id)
    )
from fastapi import APIRouter, Depends
from app.dependancies import get_company

from app.schemas.profile import ProfileResponse
from app.services.profile_service import get_profile

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
def company(info: depends(get_company)):
    return info 
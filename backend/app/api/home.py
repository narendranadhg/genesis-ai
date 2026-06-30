from fastapi import APIRouter

from app.schemas.profile import get_profile

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


@router.get("/profile", response_model=ProfileResponse)

def profile():
    return get_profile()
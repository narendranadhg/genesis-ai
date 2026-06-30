from fastapi import APIRouter

from app.schemas.profile import ProfileResponse

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
    return ProfileResponse(
        company="Genesis AI",
        founder="Narendranadh G",
        version="1.0",
        mission="Build Enterprise AI Solutions"
    )
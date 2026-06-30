from app.schemas.profile import ProfileResponse

def get_profile() -> ProfileResponse:
    return ProfileResponse(
        company="Genesis AI",
        founder="Narendranadh G",
        version="1.0",
        mission="Build Enterprise AI Solutions"
    )
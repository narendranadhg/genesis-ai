from pydantic import BaseModel

class ProfileResponse(BaseModel):
    company: str
    founder: str
    version: str
    mission: str
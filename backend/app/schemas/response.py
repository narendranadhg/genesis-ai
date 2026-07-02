from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Any = None
    timestamp: datetime = Field(default_factory=datetime.now)
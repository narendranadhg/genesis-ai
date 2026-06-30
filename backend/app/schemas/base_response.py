from datetime import datetime
from typing import Any

from pydantic import BaseModel


class BaseResponse(BaseModel):
    success: bool
    message: str
    data: Any = None
    timestamp: datetime
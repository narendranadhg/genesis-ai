from typing import Any

from app.schemas.base_response import BaseResponse

def success_response(
    message: str,
    data: Any = None
):
    return BaseResponse(
        success=True,
        message=message,
        data=data
    )
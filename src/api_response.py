
from pydantic import BaseModel
from typing import Any
    

class APIResponse(BaseModel):
    is_success: bool
    message: str
    status_code: int
    data: Any

from typing import List, Union
from pydantic import BaseModel
from uuid import UUID, uuid4
from enum import Enum

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"

class Role(Enum):
    ADMIN = "ADMIN"
    USER = "USER"
    GUEST = "GUEST"

class User(BaseModel):
    id: Union[None, UUID] = uuid4()
    first_name: str
    last_name: str
    middle_name: Union[None, str] = None
    gender: Gender
    role: List[Role]



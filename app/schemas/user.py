from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    email: EmailStr
    is_active: bool = False


class CreateUser(UserBase):
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


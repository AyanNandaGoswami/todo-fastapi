from pydantic import BaseModel
from typing import Optional


class TodoBase(BaseModel):
    name: str
    description: Optional[str] = None
    is_completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    name: Optional[str] = None
    description: Optional[str] = None
    is_completed: bool = False


class TodoOut(TodoBase):
    id: int
    name: str

    class Config:
        orm_mode = True



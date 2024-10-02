from sqlalchemy import Column, Integer, Boolean, String
from app.dependencies.database import Base


class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)


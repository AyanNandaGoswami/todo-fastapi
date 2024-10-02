from operator import index

from sqlalchemy import Column, String, Integer, Boolean
from app.dependencies.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100), nullable=True)
    email = Column(String(75))
    password = Column(String(300))
    is_active = Column(Boolean, default=False)


from sqlalchemy import Column, String, Boolean
from src.models.base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)

    role = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    telegram_id = Column(String, nullable=False)
    image = Column(String, nullable=False)
    is_approved = Column(Boolean, nullable=False)
    image_path = Column(String, nullable=False)

    password_hash = Column(String, nullable=False)
    password_salt = Column(String, nullable=False)


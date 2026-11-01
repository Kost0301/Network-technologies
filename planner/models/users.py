from typing import List, Optional
from beanie import Document, Link
from models.events import Event
from pydantic import BaseModel, EmailStr


class User(Document):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]] = []

    class Settings:
        name = "users"  # Имя коллекции в MongoDB

    class Config:
        json_schema_extra = {
            "example": {
                "email": "student@uust.ru",
                "password": "strongpassword123",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "student@uust.ru",
                "password": "strongpassword123",
            }
        }
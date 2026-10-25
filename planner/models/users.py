from typing import List, Optional
from models.events import Event
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Event]] = []

    class Config:
        json_schema_extra = {
            "example": {
                "email": "student@uust.ru",
                "password": "StrongPassword123!",
                "events": [],
            }
        }


# Модель для регистрации нового пользователя
class NewUser(User):
    pass


# Модель для входа пользователя
class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "student@uust.ru",
                "password": "StrongPassword123!",
            }
        }
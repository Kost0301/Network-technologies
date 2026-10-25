from typing import List, Optional
from sqlmodel import Column, Field, JSON, SQLModel


# 1. Таблица событий для базы данных (table=True)
class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    image: str
    description: str
    tags: List[str] = Field(default=[], sa_column=Column(JSON))
    location: str

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "title": "Презентация БД SQLModel (Марданов Рустем)",
                "image": "https://linktomyimage.com/banner.png",
                "description": "Событие сохранено в базе данных SQLite",
                "tags": ["python", "fastapi", "sqlmodel", "sqlite"],
                "location": "УУНиТ, ауд. 301",
            }
        }


# 2. Модель для частичного обновления события (PUT)
class EventUpdate(SQLModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Обновленное название события (Марданов Рустем)",
                "location": "Новая аудитория 305",
            }
        }
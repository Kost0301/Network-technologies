from typing import List, Optional
from beanie import Document
from pydantic import BaseModel


# Модель документа для MongoDB (наследуется от Document)
class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Settings:
        name = "events"  # Имя коллекции в MongoDB

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI NoSQL Презентация (Марданов Рустем)",
                "image": "https://linktomyimage.com/image.png",
                "description": "Событие сохранено в документоориентированной базе MongoDB",
                "tags": ["fastapi", "mongodb", "beanie"],
                "location": "УУНиТ, ауд. 301",
            }
        }


# Модель для обновления
class EventUpdate(BaseModel):
    title: Optional[str] = None
    image: Optional[str] = None
    description: Optional[str] = None
    tags: Optional[List[str]] = None
    location: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Обновленное событие (Марданов Рустем)",
                "location": "Конференц-зал",
            }
        }
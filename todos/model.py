from typing import List, Optional
from fastapi import Form
from pydantic import BaseModel


class Todo(BaseModel):
    id: Optional[int] = None
    item: str

    # Метод для чтения данных из обычной HTML-формы
    @classmethod
    def as_form(cls, item: str = Form(...)):
        return cls(item=item)

    class Config:
        json_schema_extra = {
            "example": {
                "item": "Пример задачи (Марданов Рустем)",
            }
        }


class TodoItem(BaseModel):
    item: str


class TodoItems(BaseModel):
    todos: List[TodoItem]
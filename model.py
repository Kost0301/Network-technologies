from typing import List
from pydantic import BaseModel


# Базовая модель задачи с ID (для создания)
class Todo(BaseModel):
    id: int
    item: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "item": "Пример задачи (Студент: Марданов Рустем)",
            }
        }


# Модель только для текста задачи (для обновления PUT)
class TodoItem(BaseModel):
    item: str

    class Config:
        json_schema_extra = {
            "example": {"item": "Обновленный текст задачи (Марданов Рустем)"}
        }


# Модель ответа для списка задач (скрывает ID, возвращает только текст)
class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        json_schema_extra = {
            "example": {
                "todos": [
                    {"item": "Первая задача (Марданов Рустем)"},
                    {"item": "Вторая задача (Марданов Рустем)"},
                ]
            }
        }
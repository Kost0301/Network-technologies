from fastapi import APIRouter, Path
from model import Todo

todo_router = APIRouter()

# Временная база данных в памяти
todo_list = []

# 1. Добавление задачи (POST)
@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    # Персонализированный ответ (согласно Заданию 1)
    return {
        "message": "Задача успешно добавлена! (Студент: Марданов Рустем)"
    }

# 2. Получение всех задач (GET)
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {
        "todos": todo_list
    }

# 3. Получение одной задачи по ID (GET с параметром пути)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="ID задачи, которую нужно получить", ge=1)
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    return {
        "message": "Задача с таким ID не найдена. (Проверил: Марданов Рустем)"
    }
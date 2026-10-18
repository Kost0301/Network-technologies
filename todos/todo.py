from pathlib import Path
from fastapi import APIRouter, Depends, HTTPException, Path as PathParam, Request, status
from fastapi.templating import Jinja2Templates
from model import Todo

todo_router = APIRouter()

# Надежный путь к папке templates (всегда найдет папку рядом с файлом todo.py)
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Список задач в памяти
todo_list = []


# 1. Добавление задачи через форму (POST)
@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse(
        request=request, name="todo.html", context={"todos": todo_list}
    )


# 2. Получение списка всех задач (GET)
@todo_router.get("/todo")
async def retrieve_todos(request: Request):
    return templates.TemplateResponse(
        request=request, name="todo.html", context={"todos": todo_list}
    )


# 3. Просмотр отдельной задачи по ID (GET)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    request: Request,
    todo_id: int = PathParam(..., title="ID задачи", ge=1),
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request=request, name="todo.html", context={"todo": todo}
            )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с таким ID не найдена.",
    )
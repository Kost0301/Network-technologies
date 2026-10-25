from fastapi import APIRouter, HTTPException, Path, status
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

# Временное хранилище в памяти
todo_list = []


# 1. CREATE: Добавление задачи со статусом 201 Created
@todo_router.post("/todo", status_code=status.HTTP_201_CREATED)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Задача успешно создана! (Разработчик: Марданов Рустем)"
    }


# 2. READ ALL: Получение всех задач с использованием response_model
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


# 3. READ ONE: Получение задачи по ID (с выбросом ошибки 404)
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(
    todo_id: int = Path(..., title="ID запрашиваемой задачи", ge=1),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {"todo": todo}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с таким ID не найдена. (Проверил: Марданов Рустем)",
    )


# 4. UPDATE: Обновление задачи по ID (PUT)
@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_data: TodoItem,
    todo_id: int = Path(..., title="ID обновляемой задачи", ge=1),
) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item
            return {
                "message": "Задача успешно обновлена! (Разработчик: Марданов Рустем)"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Невозможно обновить: задача не найдена. (Проверил: Марданов Рустем)",
    )


# 5. DELETE ONE: Удаление задачи по ID
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int = Path(..., ge=1)) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Задача успешно удалена! (Разработчик: Марданов Рустем)"
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Невозможно удалить: задача не найдена. (Проверил: Марданов Рустем)",
    )


# 6. DELETE ALL: Очистка всех задач
@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {"message": "Все задачи очищены! (Разработчик: Марданов Рустем)"}
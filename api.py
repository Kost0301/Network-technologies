from fastapi import FastAPI
from todo import todo_router

app = FastAPI(title="Todo API - Практическая работа №4")

# Главный маршрут
@app.get("/")
async def welcome() -> dict:
    return {"message": "Добро пожаловать в Todo API! Автор: Марданов Русетем"}

# Подключаем маршрутизатор задач к главному приложению
app.include_router(todo_router)
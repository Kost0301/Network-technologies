from database.connection import conn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.events import event_router
from routes.users import user_router
import uvicorn

app = FastAPI(title="Event Planner с базой данных SQLite — ПЗ №8")

# Подключение роутеров
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")


# Событие запуска сервера: автоматически создаст файл базы planner.db и таблицу event
@app.on_event("startup")
def on_startup():
    conn()


@app.get("/")
async def home():
    return RedirectResponse(url="/event/")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
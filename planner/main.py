from contextlib import asynccontextmanager
from database.connection import Settings
from fastapi import FastAPI
from routes.events import event_router
from routes.users import user_router
import uvicorn

settings = Settings()


# Асинхронная инициализация базы при старте
@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield


app = FastAPI(
    title="Event Planner с NoSQL (MongoDB + Beanie)", lifespan=lifespan
)

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
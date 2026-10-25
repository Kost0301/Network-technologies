from models.events import Event
from sqlmodel import Session, SQLModel, create_engine

# Имя файла базы данных SQLite
database_file = "planner.db"
database_connection_string = f"sqlite:///{database_file}"

# check_same_thread: False обязателен для работы SQLite в асинхронном FastAPI
connect_args = {"check_same_thread": False}
engine_url = create_engine(
    database_connection_string, echo=True, connect_args=connect_args
)


# Функция инициализации таблиц при старте
def conn():
    SQLModel.metadata.create_all(engine_url)


# Функция-генератор сессий для маршрутов (Depends)
def get_session():
    with Session(engine_url) as session:
        yield session
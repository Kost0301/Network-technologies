from typing import Any, List, Optional
from beanie import PydanticObjectId, init_beanie
from models.events import Event
from models.users import User
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings

# 🛠️ Исправление бага несовместимости Beanie и Motor в Python 3.13:
AsyncIOMotorClient.append_metadata = lambda *args, **kwargs: None


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = "mongodb://localhost:27017/planner"

    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        # Явно указываем базу данных 'planner'
        await init_beanie(
            database=client.planner,
            document_models=[Event, User],
        )

    class Config:
        env_file = ".env"


# Универсальный класс для CRUD операций
class Database:

    def __init__(self, model):
        self.model = model

    async def save(self, document) -> None:
        await document.create()
        return

    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False

    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs

    async def update(self, id: PydanticObjectId, body: Any) -> Any:
        doc_id = id
        des_body = body.model_dump(exclude_unset=True)
        update_query = {
            "$set": {
                field: value
                for field, value in des_body.items()
                if value is not None
            }
        }
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc

    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True
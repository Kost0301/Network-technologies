from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, HTTPException, status
from models.events import Event, EventUpdate

event_router = APIRouter(tags=["Events"])
event_database = Database(Event)


# 1. Получить все события
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events() -> List[Event]:
    events = await event_database.get_all()
    return events


# 2. Получить событие по ObjectID
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: PydanticObjectId) -> Event:
    event = await event_database.get(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено в MongoDB",
        )
    return event


# 3. Создать событие
@event_router.post("/new")
async def create_event(body: Event) -> dict:
    await event_database.save(body)
    return {
        "message": "Событие успешно сохранено в MongoDB! (Автор: Марданов Рустем)"
    }


# 4. Обновить событие (PUT)
@event_router.put("/{id}", response_model=Event)
async def update_event(id: PydanticObjectId, body: EventUpdate) -> Event:
    updated_event = await event_database.update(id, body)
    if not updated_event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено в MongoDB",
        )
    return updated_event


# 5. Удалить событие (DELETE)
@event_router.delete("/{id}")
async def delete_event(id: PydanticObjectId) -> dict:
    event = await event_database.delete(id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с указанным ID не найдено в MongoDB",
        )
    return {"message": "Событие успешно удалено из MongoDB!"}
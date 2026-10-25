from typing import List
from database.connection import get_session
from fastapi import APIRouter, Depends, HTTPException, status
from models.events import Event, EventUpdate
from sqlmodel import select

event_router = APIRouter(tags=["Events"])


# 1. CREATE: Создание события и сохранение в SQLite (стр. 6)
@event_router.post("/new")
async def create_event(
    new_event: Event, session=Depends(get_session)
) -> dict:
    session.add(new_event)
    session.commit()
    session.refresh(new_event)
    return {
        "message": f"Событие '{new_event.title}' успешно сохранено в БД! (Автор: Марданов Рустем)"
    }


# 2. READ ALL: Получение всех событий из SQLite (стр. 7)
@event_router.get("/", response_model=List[Event])
async def retrieve_all_events(session=Depends(get_session)) -> List[Event]:
    statement = select(Event)
    events = session.exec(statement).all()
    return events


# 3. READ ONE: Получение события по ID из SQLite (стр. 7)
@event_router.get("/{id}", response_model=Event)
async def retrieve_event(id: int, session=Depends(get_session)) -> Event:
    event = session.get(Event, id)
    if event:
        return event
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Событие с таким ID не найдено в базе данных",
    )


# 4. UPDATE: Редактирование события по ID (стр. 8–9)
@event_router.put("/edit/{id}", response_model=Event)
async def update_event(
    id: int, new_data: EventUpdate, session=Depends(get_session)
) -> Event:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие для обновления не найдено в БД",
        )

    # Исключаем незаполненные поля
    event_data = new_data.model_dump(exclude_unset=True)
    for key, value in event_data.items():
        setattr(event, key, value)

    session.add(event)
    session.commit()
    session.refresh(event)
    return event


# 5. DELETE: Удаление события из SQLite (стр. 9)
@event_router.delete("/delete/{id}")
async def delete_event(id: int, session=Depends(get_session)) -> dict:
    event = session.get(Event, id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Событие с таким ID не найдено для удаления",
        )
    session.delete(event)
    session.commit()
    return {
        "message": f"Событие с ID {id} успешно удалено из БД! (Марданов Рустем)"
    }
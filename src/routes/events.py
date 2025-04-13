from fastapi import APIRouter
from src.models.events import Event

event_router = APIRouter(
    prefix="/events",
    tags=["events"]
)
events: list[Event] = []

@event_router.get("/", response_model=list[Event])
async def get_all_events():
    return events

@event_router.get("/{id}")
async def get_event(id: int):
    for event in events:
        if event.id == id:
            return event
    return {"message": "Event not found"}

@event_router.post("/")
async def post_event(event: Event):
    events.append(event)
    return {"message": "Event created successfully"}

@event_router.delete("/{id}")
async def delete_event(id: int):
    for event in events:
        if event.id == id:
            events.remove(event)
            return {"message": "Event deleted successfully"}
    return {"message": "Event not found"}

@event_router.put("/{id}")
async def update_event(id: int, event: Event):
    for i, e in enumerate(events):
        if e.id == id:
            events[i] = event
            return {"message": "Event updated successfully"}
    return ""
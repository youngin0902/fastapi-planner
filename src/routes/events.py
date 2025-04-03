from fastapi import APIRouter

event_router = APIRouter(
    prefix="/events",
    tags=["Events"]
)

@event_router.post("/")
async def get_all_events():
    return[]

@event_router.get("/{id}")
async def get_event():
    return""

@event_router.post("/")
async def post_event():
    return ""

@event_router.put("/{id")
async def update_event():
    return ""

@event_router.delete("/{id}")
async def delete_event():
    return ""


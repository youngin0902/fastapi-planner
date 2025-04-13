from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routes.events import event_router
from .routes.users import user_router
from .database.connection import Settings


settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield

app = FastAPI(
    lifespan=lifespan
)
app.include_router(event_router)
app.include_router(user_router)


@app.get("/")
async def root_path():
    return "hello world!"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main.app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from beanie import Document, init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional, List
from pydantic import Field
from datetime import datetime
from contextlib import asynccontextmanager

# MongoDB 설정
MONGODB_URL = "mongodb://localhost:27017"
DB_NAME = "test_db"


# MongoDB 모델 정의
class Item(Document):
    id: UUID = Field(default_factory=uuid4)
    description: Optional[str] = Field(default=None, description="아이템 설명")
    price: float = Field(gt=0, description="가격은 0보다 커야 합니다")
    tax: Optional[float] = Field(default=None, ge=0, description="세금")
    created_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "items"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 실행
    client = AsyncIOMotorClient(MONGODB_URL)
    await init_beanie(database=client[DB_NAME], document_models=[Item])
    yield
    # 종료 시 실행
    client.close()


app = FastAPI(lifespan=lifespan)

# app.on_event는 레거시 -> lifespan으로 만들어야함
@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI with Beanie and MongoDB"}


@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Item:
    try:
        await item.insert()
        return item
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/items/", response_model=List[Item])
async def get_items(skip: int = 0, limit: int = 10) -> List[Item]:
    try:
        items = await Item.find_all().skip(skip).limit(limit).to_list()
        return items
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

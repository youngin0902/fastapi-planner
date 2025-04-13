from pydantic import BaseModel, ConfigDict
from beanie import Document

class Event(Document):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "아 졸리다..",
                "imate": "path",
                "description": "돈많은 백수되고싶다",
                "tags": ["#귀찮다", "#졸리다"],
                "location": "제1 실습관",
                "created_at": "2019-09-22"
            }
        }
    )
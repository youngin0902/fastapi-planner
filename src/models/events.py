from pydantic import BaseModel, EmailStr, ConfigDict

class Event(BaseModel):
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
                "title": "아.. 졸리다",
                "image": "path/to",
                "description": "아진짜싫다..",
                "tags": ["#귀차니즘", "#강의"],
                "location": "실습관"
            }
        }
    )

class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] | None = None

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

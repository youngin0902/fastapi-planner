from pydantic import BaseModel, EmailStr
from beanie import Document
from .events import Event

class User(Document):
    email: EmailStr
    password: str
    events: list[Event] | None = None

    class Settings:
        name = "users"

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

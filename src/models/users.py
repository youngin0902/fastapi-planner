from pydantic import BaseModel, EmailStr
from events import Event  # event.py 파일에 정의된 Event 클래스를 임포트

class User(BaseModel):
    email: EmailStr
    password: str
    events: list[Event] | None = None

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

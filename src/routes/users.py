from fastapi import APIRouter

user_router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@user_router.post("/signup")
async def sign_new_user():
    return "not implemented"

@user_router.post("/signin")
async def sign_user_in():
    return "not implemented"
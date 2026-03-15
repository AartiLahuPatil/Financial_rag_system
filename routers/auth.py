from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

class User(BaseModel):
    username: str
    password: str

users = {}

@router.post("/register")
def register(user: User):

    if user.username in users:
        return {"message": "User already exists"}

    users[user.username] = user.password

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: User):

    if user.username not in users:
        return {"message": "User not found"}

    if users[user.username] != user.password:
        return {"message": "Incorrect password"}

    return {"message": "Login successful"}
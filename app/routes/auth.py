from app.utils.database import db
from app.models.users import UserRegister, UserLogin
from fastapi import APIRouter, HTTPException
from app.utils import auth

auth_router = APIRouter()


@auth_router.post("/register")
def register(user: UserRegister):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=406, detail="Email already exists")

    user_password = auth.get_password_hash(user.password)

    db.users.insert_one(
        {"name": user.name, "email": user.email, "password": user_password}
    )
    access_token = auth.create_access_token(data={"sub": user.email})
    return {"token": access_token, "token_type": "bearer"}


@auth_router.post("/login")
def login(user: UserLogin):
    user_data = db.users.find_one({"email": user.email})
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    if user_data["password"] != user.password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    access_token = auth.create_access_token(data={"sub": user.email})

    return {"token": access_token, "token_type": "bearer"}

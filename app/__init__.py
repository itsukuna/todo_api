from fastapi import FastAPI
from app.routes.auth import auth_router
from app.routes.todos import todo_router


app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(todo_router, prefix="/todos", tags=["Todos"])

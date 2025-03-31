from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

from fastapi import APIRouter, HTTPException, Depends
from app.models.todos import Todo, TodoUpdate
from app.utils.database import db
from app.utils.auth import get_current_user
from bson import ObjectId

todo_router = APIRouter()


@todo_router.post("/")
def create_todo(todo: Todo, user: dict = Depends(get_current_user)):
    todo_data = todo.model_dump()
    todo_data["user_id"] = user["email"]
    result = db.todos.insert_one(todo_data)
    return {"message": "Todo created successfully", "id": str(result.inserted_id)}


@todo_router.get("/")
def get_todos(user: dict = Depends(get_current_user)):
    todos = list(db.todos.find({"user_id": user["email"]}))
    for todo in todos:
        todo["_id"] = str(todo["_id"])
    return todos


@todo_router.get("/{todo_id}")
def get_todo(todo_id: str, user: dict = Depends(get_current_user)):
    todo = db.todos.find_one({"_id": ObjectId(todo_id), "user_id": user["email"]})
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo["_id"] = str(todo["_id"])
    return todo


@todo_router.put("/{todo_id}")
def update_todo(todo_id: str, todo: TodoUpdate, user: dict = Depends(get_current_user)):
    todo_data = todo.model_dump(exclude_unset=True)
    result = db.todos.update_one(
        {"_id": ObjectId(todo_id), "user_id": user["email"]}, {"$set": todo_data}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo = db.todos.find_one(
        {"_id": ObjectId(todo_id), "user_id": user["email"]}
    )
    updated_todo["_id"] = str(updated_todo["_id"])
    return {"message": "Todo updated successfully", "todo": updated_todo}


@todo_router.delete("/{todo_id}")
def delete_todo(todo_id: str, user: dict = Depends(get_current_user)):
    result = db.todos.delete_one({"_id": ObjectId(todo_id), "user_id": user["email"]})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}

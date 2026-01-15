from fastapi import FastAPI
from typing import List
from uuid import uuid4, UUID

from . import models

app = FastAPI()


database: List[models.User] = [
    models.User(id=uuid4(), first_name="tyler", last_name="durden", gender=models.Gender.MALE, role=[models.Role.USER]),
    models.User(id=uuid4(), first_name="edward", last_name="norton", gender=models.Gender.MALE, role=[models.Role.ADMIN]),
    models.User(id=uuid4(), first_name="anne", last_name="hathway", gender=models.Gender.FEMALE, role=[models.Role.GUEST])
]


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/users")
def get_users():
    return {"message": database}    

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for id in range(len(database)):
        if id + 1 == user_id:
            return {"message": database[user_id - 1]}
    
    return {"message": "User not found"}

@app.post("/users")
def create_user(user: models.User):
    for id in range(len(database)):
        if database[id].first_name == user.first_name and database[id].last_name == user.last_name:
            return {
                "message": "failure",
                "status": 409,
                "data": "User already exists"
            }

    database.append(user)
    return {
        "message": "success",
        "status": 201,
        "data": user
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    for user in database:
        print(user.id, user_id)
        if user.id == UUID(user_id):
            print(user.id, user_id)
            database.remove(user)
            return {
                "message": "success",
                "status": 200,
                "data": "User deleted"
            }
    
    return {
        "message": "failure",
        "status": 404,
        "data": "User Not Found"
    }







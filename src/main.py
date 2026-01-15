from fastapi import FastAPI, HTTPException
from typing import List
from uuid import uuid4, UUID

from . import models
from . import api_response

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
    
    raise HTTPException(status_code=404, detail="User not found")
    # return {"message": "User not found"}

@app.post("/users")
def create_user(user: models.User):
    for id in range(len(database)):
        if database[id].first_name == user.first_name and database[id].last_name == user.last_name:
            raise HTTPException(status_code=409, detail="User already exists")
            # return {
            #     "message": "failure",
            #     "status": 409,
            #     "data": "User already exists"
            # }

    database.append(user)
    return {
        "message": "success",
        "status": 201,
        "data": user
    }

@app.delete("/users/{user_id}")
def delete_user(user_id: str):
    for user in database:
        if user.id == UUID(user_id):
            database.remove(user)
            return {
                "message": "success",
                "status": 200,
                "data": "User deleted"
            }
    
    raise HTTPException(status_code=404, detail="User not found")
    # return {
    #     "message": "failure",
    #     "status": 404,
    #     "data": "User Not Found"
    # }

@app.put("/users/{user_id}")
def update_user(user_id: str, update_user: models.Update_User):
    for user in database:
        if user.id == UUID(user_id):
            if update_user.first_name != None:
                user.first_name = update_user.first_name
            if update_user.last_name != None:
                user.last_name = update_user.last_name
            if update_user.middle_name:
                user.middle_name = update_user.middle_name
            if update_user.role:
                user.role = update_user.role

            return api_response.APIResponse(is_success=True, message="User found", status_code=200, data=user)

            # return {
            #     "message": "success",
            #     "status": 200,
            #     "data": user
            # }

    raise HTTPException(status_code=404, detail="User not found")





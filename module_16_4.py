from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
def get_all_messages() -> List[User]:
    return users


@app.post("/user/{username}/{age}")
def create_message(user: User) -> User:
    l = len(users)
    l1 = 1
    if l > 0:
        l1 = users[l - 1].id + 1
    user.id = l1
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
def update_messages(user_id: int, username: str, age: int) -> User:
    try:
        for i in users:
            if i.id == user_id:
                i.username = username
                i.age = age
                return i
        k = 5 / 0
    except ZeroDivisionError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
def delete_massege(user_id: int) -> User:
    try:
        k = 0
        for i in users:
            if i.id == user_id:
                return users.pop(k)
            k += 1
        edit_message = users[k]
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")

from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates=Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html",{"request":request, "users":users})


@app.get(path="/user/{user_id}")
def get_all_messages(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html",{"request":request, "user":users[user_id-1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")


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

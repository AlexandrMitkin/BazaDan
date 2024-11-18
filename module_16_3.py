from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# @app.get("/")
# async def welcome() -> dict:
#     return {"massege": "Главная страница"}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_messages(username: str, age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_messages(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_massege(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"

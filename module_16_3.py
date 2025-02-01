from http.client import HTTPException
from fastapi import HTTPException
from fastapi import FastAPI, Path
from typing import Annotated

from fastapi.openapi.utils import status_code_ranges

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


# @app.get("/")
# async def welcome() -> dict:
#     return {"massege": "Главная страница"}


@app.get("/users")
async def get_all_messages() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_messages(username: str= Path(min_length=3, max_length=15, description="Enter your name", example="Vasya"),
                          age: int=Path(ge=1, le=100, description="Enter your age", example="18")) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = f"Имя: {username}, возраст: {age}"
    return f"User {current_index} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_messages(user_id: str,
                          username: Annotated[str,Path(min_length=3, max_length=15, description="Enter your name", example="Vasya")],
                          age: Annotated[int,Path(ge=1, le=100, description="Enter your age", example="18")]) -> str:
    for i in users:
        if i[0]==user_id:
            users[user_id] = f"Имя: {username}, возраст: {age}"
            return f"The user {user_id} is updated"
    raise HTTPException(status_code=404, detail="user not found")



@app.delete("/user/{user_id}")
async def delete_massege(user_id: str) -> str:
    for i in users:
        if i[0]==user_id:
            users.pop(user_id)
            return f"User {user_id} has been deleted"
    raise HTTPException(status_code=404, detail="user not found")

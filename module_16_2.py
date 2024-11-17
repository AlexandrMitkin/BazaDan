from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"massege": "Главная страница"}


@app.get("/user/admin")
async def welcome_admin() -> dict:
    return {"massege": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def welcome_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="1")) -> dict:
    return {"massege": f"Вы вошли как пользователь № {user_id}"}


@app.get("/user/{username}/{age}")
async def info_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", example="UrbanUser")]
        , age: int = Path(ge=18, le=120, description="Enter age", example="24")) -> dict:
    return {"massege": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

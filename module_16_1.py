from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"massege":"Главная страница"}

@app.get("/user/admin")
async def welcome_admin() -> dict:
    return {"massege":"Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def welcome_user(user_id: int) -> dict:
    return {"massege":f"Вы вошли как пользователь №{user_id}"}

@app.get("/user")
async def info_user(username: str="Ilya", age:int=24) -> dict:
    return {"massege":f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
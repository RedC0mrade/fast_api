from fastapi import FastAPI

from starlette.responses import FileResponse

from models import User

app = FastAPI()


@app.get('/')
async def root():
    return FileResponse('../index.html')


@app.post('/calculate')
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


@app.post("/users")
def user(age: int, name: str):
    return User(name=name, age=age, is_adult=(age >= 18))

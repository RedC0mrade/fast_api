from fastapi import FastAPI

from starlette.responses import FileResponse

from models import User

app = FastAPI()
messages = []

@app.get('/')
async def root():
    return FileResponse('../index.html')


@app.post('/calculate')
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


@app.post("/users")
async def user(age: int, name: str):
    return User(name=name, age=age, is_adult=(age >= 18))


@app.post('/feedback')
async def feedback(name: str, message: str):
    messages.append({name: message})
    return {"message": "Feedback received. Thank you, Alice!"}

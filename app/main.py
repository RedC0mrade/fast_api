from fastapi import FastAPI

from starlette.responses import FileResponse

from models import UserCreate, Feedback

app = FastAPI()
messages = []

@app.get('/')
async def root():
    return FileResponse('../index.html')


@app.post('/calculate')
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


@app.post("/user_create")
async def user_create(user: UserCreate):
    return user


@app.post('/feedback')
async def feedback(feedback: Feedback):
    messages.append({feedback.name: feedback.message})
    return {"message": "Feedback received. Thank you, Alice!"}

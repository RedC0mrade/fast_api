from fastapi import FastAPI
from datetime import datetime
from typing import List, Union

from pydantic import BaseModel
from starlette.responses import FileResponse

app = FastAPI()





@app.get('/')
async def root():
    return FileResponse('../index.html')


@app.post('/calculate')
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}


@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

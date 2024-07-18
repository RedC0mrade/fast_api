from fastapi import FastAPI
from starlette.responses import FileResponse, JSONResponse

app = FastAPI()


@app.get('/')
async def root():
    return FileResponse('index.html')


@app.post('/calculate')
async def calculate(num1: int, num2: int):
    return {"result": num1 + num2}

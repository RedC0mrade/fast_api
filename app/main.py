from fastapi import FastAPI, Response

from starlette.responses import FileResponse

from models import SampleProduct, UserLogin, UserCreate, Feedback

app = FastAPI()
messages = []

data_base = [SampleProduct(product_id=456, name='Phone Case', category='Accessories', price=19.99),
             SampleProduct(product_id=101, name='Headphones', category='Accessories', price=99.99),
             SampleProduct(product_id=789, name='Iphone', category='Electronics', price=1299.99),
             SampleProduct(product_id=123, name='Smartphone', category='Electronics', price=599.99)]

user_base = [UserLogin(username='QQQ', login='qqq', token=None),
             UserLogin(usrname='WWW', login='www', token=None)]


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


@app.post('/product_create')
async def product_create(samply_product: SampleProduct):
    data_base.append(samply_product)
    return samply_product


@app.get('/product/{product_id}')
async def get_product(product_id: int):
    for product in data_base:
        if product.product_id == product_id:
            return product


@app.get('/products/search')
async def product_search(keyword: str, category: str | None = None, limit: int = 10):
    search_result = list(filter(lambda x: keyword in x.name, data_base))
    if category:
        category_result = list(filter(lambda x: x.category == category, search_result))
        return category_result[:limit]
    return search_result[:limit]

@app.post('/login')
async def user_login(user_login: UserLogin):

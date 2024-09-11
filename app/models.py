from pydantic import BaseModel


class UserLogin(BaseModel):
    """Login models"""
    username: str
    password: str
    token: str | None = None


class UserCreate(BaseModel):
    """User models"""
    age: int
    email: str
    name: str
    is_subscribed: bool = False


class SampleProduct(BaseModel):
    product_id: int
    name: str
    category: str
    price: float


class Feedback(BaseModel):
    """Message model"""
    name: str
    message: str

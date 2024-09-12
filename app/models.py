from pydantic import BaseModel


class UserLogin(BaseModel):
    """Login model"""
    username: str
    password: str
    token: str | None = None


class UserCreate(BaseModel):
    """User model"""
    age: int
    email: str
    name: str
    is_subscribed: bool = False


class SampleProduct(BaseModel):
    """Product model"""
    product_id: int
    name: str
    category: str
    price: float


class Feedback(BaseModel):
    """Message model"""
    name: str
    message: str

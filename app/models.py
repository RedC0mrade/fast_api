from pydantic import BaseModel


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

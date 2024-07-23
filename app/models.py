from pydantic import BaseModel


class UserCreate(BaseModel):
    """User models"""
    age: int
    email: str
    name: str
    is_subscribed: bool = False


class Feedback(BaseModel):
    """Message model"""
    name: str
    message: str

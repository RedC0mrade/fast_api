from pydantic import BaseModel


class User(BaseModel):
    """User models"""
    age: int
    name: str
    is_adult: bool = False

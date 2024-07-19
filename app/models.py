from pydantic import BaseModel


class User(BaseModel):
    """User models"""

    id: int
    name: str


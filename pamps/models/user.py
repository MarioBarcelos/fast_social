from typing import Optional, List, TYPE_CHECKING
from sqlmodel import Field, SQLModel, Relationship
from pamps.security import HashedPassword
from pydantic import BaseModel

if TYPE_CHECKING:
    from pamps.models.post import Post

class User(SQLModel, table=True):
    """Tabela de Usuário"""

    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True, nullable=False)
    avatar: Optional[str] = Field(default=None, unique=True)
    bio: Optional[str] = None
    password: HashedPassword

    posts: List["Post"] = Relationship(back_populates="user")

class UserResponse(BaseModel):
    """Serializer for user response"""
    username: str
    avatar: Optional[str] = None
    bio: Optional[str] = None

class UserRequest(SQLModel):
    username: str
    email: str
    password: str
    avatar: Optional[str] = None
    bio: Optional[str] = None

    class Config:
        from_attributes = True
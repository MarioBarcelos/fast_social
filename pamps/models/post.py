from datetime import datetime
from typing import TYPE_CHECKING, Optional
from pydantic import BaseModel, Extra
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from pamps.models.user import User

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    text: str
    date: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    user_id: Optional[int] = Field(foreign_key="user.id")
    parent_id: Optional[int] = Field(foreign_key="post.id")

    user: Optional["User"] = Relationship(back_populates="posts")

    parent: Optional["Post"] = Relationship(
        back_populates="replies",
        sa_relationship_kwargs=dict(remote_side="Post.id"),
    )

    replies: list["Post"] = Relationship(back_populates="parent")

    def __lt__(self, other):
        return self.date < other.date
    
class PostResponse(BaseModel):
    """Serializer Post Response"""

    id: int
    text: str
    date: datetime
    user_id: int
    parent_id: Optional[int]

class PostResponseWithReplies(PostResponse):
    replies: Optional[list["PostResponse"]] = None

    class Config:
        from_attributes = True

class PostRequest(BaseModel):
    """Serializer Post Request payload"""

    parent_id: Optional[int]
    text: str 

    class Config:
        extra = Extra.allow
        arbitrary_types_allowed = True

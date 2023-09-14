from .database import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List, Optional
import datetime

class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    username: Mapped[str] = mapped_column(db.String(1000), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(1000), nullable=False)
    posts: Mapped[List["Post"]] =  db.relationship(back_populates="user")
    
class Post(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    author_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user: Mapped["User"] = db.relationship(back_populates="posts")
    created: Mapped[datetime.datetime] = mapped_column(db.DateTime, nullable=False, server_default=db.text('CURRENT_TIMESTAMP'))
    title: Mapped[str] = mapped_column(db.String(1000), nullable=False)
    body: Mapped[Optional[str]] = mapped_column(db.String(1000000))
    

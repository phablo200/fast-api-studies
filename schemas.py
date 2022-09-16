from typing import List
from pydantic import BaseModel

class Article(BaseModel):
  title: str
  content: str
  published: bool
  class Config():
    orm_mode = True

class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  id: int
  username: str
  email: str
  items: List[Article] = []
  class Config():
    orm_mode = True

class UserArticle(BaseModel):
  id: int
  username: str
  class Config():
    orm_mode = True

class ArticleBase(BaseModel):
  title: str
  content: str
  published: bool
  creator_id: int

class ArticleDisplay(BaseModel):
  title: str
  content: str
  published: bool
  user: UserArticle
  class Config():
    orm_mode = True





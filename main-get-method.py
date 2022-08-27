from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def index():
  return {'message': 'Hello World'}

@app.post('/')
def test():
  return  'My Test'

class BlogType(str, Enum):
  short = 'short'
  story = 'story'
  howto = 'howto'

@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
  return {'message': f'I am a blog type {type}'}

@app.get('/blog/all')
def get_all_blog(page: int = 1, page_size: Optional[int] = None):
  return {'message': f'I am all blogs {page} and page_size {page_size}'}

@app.get('/blog/{id}/comments/{comment_id}')
def get_comments(id: int, comment_id: int, valid: bool = True, username: Optional[str] = None):
  return {'message': f'blog_id: {id}, comment_id: {comment_id}, valid: {valid}, username: {username}'}

@app.get('/blog/{id}', status_code=404)
def blog(id: int):
  return {'message': f'I am a blog {id}'}



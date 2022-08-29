from typing import Optional, List
from fastapi import APIRouter, Query, Body
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])

class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: int
  published: Optional[bool]

@router.post('/')
def create_blog(blog: BlogModel):
  return {'message': 'ok'}


@router.post('/edit/{id}')
def edit_blog(blog: BlogModel, id: int, version: int = 1):
  return {
    'blog': blog,
    'id': id,
    'version': version
  }

@router.post('/new/{id}/comment')
def create_comment(
  blog: BlogModel, 
  id: int, 
  comment_id: int = Query(None, 
    title='Id of the comment',
    description='Some description for comment_id',
    alias='commentId',
    deprecated=True
  ),
  content: str = Body(
    ..., 
    min_length=1, 
    max_length=12,
    regex='[a-z]'
  ),
  v: Optional[List[str]] = Query(['default1'])
):
  return {
    'blog': blog,
    'id': id,
    'comment_id': comment_id,
    'content': content,
    'version': v
  }
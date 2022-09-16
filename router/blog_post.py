from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(prefix='/blog', tags=['blog'])

class Image(BaseModel):
  url: str
  alias: str

class BlogModel(BaseModel):
  title: str
  content: str
  nb_comments: int
  published: Optional[bool]
  tags: List[str] = []
  metadata: Dict[str, str] = {}
  image: Image


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

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(
  blog: BlogModel, 
  id: int, 
  comment_title: int = Query(None, 
    title='Id of the comment',
    description='Some description for comment_title',
    alias='commentTitle',
    deprecated=True
  ),
  content: str = Body(
    ..., 
    min_length=1, 
    max_length=12,
    regex='[a-z]'
  ),
  comment_id: int = Path(None, ge=5, le=10),
  v: Optional[List[str]] = Query(['default1'])
):
  return {
    'blog': blog,
    'id': id,
    'comment_title': comment_title,
    'commend_id': comment_id,
    'content': content,
    'version': v
  }

def required_functionally():
  return {'message': 'Learning FastAPI is important'}
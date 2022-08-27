from typing import Optional
from fastapi import FastAPI, status, Response
from enum import Enum

app = FastAPI()
 
@app.get(
  '/blog/all', 
  tags=['blog'], 
  summary='Retrieve all blogs',
  description='This api call simulates fetching all blogs'
)
def get_all_blog(page: int = 1, page_size: Optional[int] = None):
  return {'message': f'I am all blogs {page} and page_size {page_size}'}

@app.get('/blog/{id}', tags=['blog'], status_code=status.HTTP_200_OK)
def blog(id: int, response: Response):
  """
    Simulates retrieving all the blogs
    - **is** is mandathory
  """
  if id > 5:
    response.status_code = status.HTTP_404_NOT_FOUND
    return {'error': f'Blog {id} not found'}
  else:
    return {'message': f'Blog with id: {id}'}




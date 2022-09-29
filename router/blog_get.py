import time
from typing import Optional
from fastapi import APIRouter, status, Response, Depends

from router.blog_post import required_functionally
from custom_log import log


router = APIRouter(
  prefix='/blog',
  tags=['blog']
)

async def time_consuming_functionality():
  time.sleep(10)
  return 'ok'

@router.get(
  '/all',  
  summary='Retrieve all blogs',
  description='This api call simulates fetching all blogs'
)
async def get_all_blog(page: int = 1, page_size: Optional[int] = None, req_parameter: dict = Depends(required_functionally)):
  await time_consuming_functionality()
  #log('MyTest', 'call to get all saproducts')
  
  return {
    'message': f'I am all blogs {page} and page_size {page_size}',
    'required_parameters': req_parameter
  }

@router.get('/{id}', status_code=status.HTTP_200_OK)
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

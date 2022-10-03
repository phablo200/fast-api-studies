from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.param_functions import Depends

router = APIRouter(
  prefix='/dependencies',
  tags=['/dependencies']
)

def convert_headers(request: Request, separator: str = '--', user: str = 'Phablo'):
  out_headers = []
  for key, value in request.headers.items():
    out_headers.append(f'{key} {separator} {value}')

  return {
    'items': out_headers,
    'user': user
  }


@router.get('/alive')
def alive():
  return {
    'description': 'Alive'
  }

@router.get('')
def get_items(headers = Depends(convert_headers)):
  return {
    'description': 'Get Items',
    'headers': headers
  }

class Account:
  def __init__(self, name: str, email: str):
    self.name = name
    self.email = email

@router.post('/user')
def create_user(name: str, email: str, password: str, account: Account = Depends()):
  return {
    'name': account.name,
    'email': account.email
  }



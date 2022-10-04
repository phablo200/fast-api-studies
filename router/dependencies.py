from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.param_functions import Depends
from custom_log import log

router = APIRouter(
  prefix='/dependencies',
  tags=['/dependencies'],
  dependencies=[Depends(log)]
)

def convert_queries(request: Request, separator: str = '--'):
  out_query = []
  for key, value in request.query_params.items():
    out_query.append(f'{key} {separator} {value}')

  return out_query

def convert_headers(request: Request, separator: str = '--', query = Depends(convert_queries)):
  out_headers = []
  for key, value in request.headers.items():
    out_headers.append(f'{key} {separator} {value}')

  return {
    'headers': out_headers,
    'query': query
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



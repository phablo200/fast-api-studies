from typing import List
from fastapi.params import Depends
from schemas import UserBase, UserDisplay
from fastapi import APIRouter
from sqlalchemy.orm import Session
from db.database import get_db
from db.db_user import create_user, get_all_users, get_user, update_user, destroy_user

router = APIRouter(
  prefix='/user',
  tags=['user']
)

@router.get('/alive')
def alive():
  return {"message": "I am alive"}

@router.get('/', response_model=List[UserDisplay])
def index(db: Session = Depends(get_db)):
  return get_all_users(db) 

@router.get('/{id}', response_model=UserDisplay)
def find(id: int, db: Session = Depends(get_db)):
  return get_user(db, id)

@router.post('/', response_model=UserDisplay)
def store(request: UserBase, db: Session = Depends(get_db)):
  return create_user(db, request)

@router.put('/{id}')
def update(id: int, request: UserBase, db: Session = Depends(get_db)):
  return update_user(db, id, request)

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
  return destroy_user(db, id)
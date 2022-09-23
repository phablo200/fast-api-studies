from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import ArticleDisplay, ArticleBase, UserBase
from db.database import get_db
from db.db_article import create_article, get_article
from auth.oauth2 import oauth2_scheme, get_current_user


router = APIRouter(
  prefix='/article',
  tags=['article']
)

@router.post('/', response_model = ArticleDisplay)
def store(request: ArticleBase, db: Session = Depends(get_db), _: UserBase = Depends(get_current_user)):
  return create_article(db, request)

@router.get('/{id}') #,response_model = ArticleDisplay)
def get(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
  return {
    'data': get_article(db, id),
    'current_user': current_user
  }


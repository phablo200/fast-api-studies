from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas import ArticleDisplay, ArticleBase
from db.database import get_db
from db.db_article import create_article, get_article

router = APIRouter(
  prefix='/article',
  tags=['article']
)

@router.post('/', response_model = ArticleDisplay)
def store(request: ArticleBase, db: Session = Depends(get_db)):
  return create_article(db, request)

@router.get('/{id}', response_model = ArticleDisplay)
def get(id: int, db: Session = Depends(get_db)):
  return get_article(db, id)



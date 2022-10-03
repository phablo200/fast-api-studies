import time
from fastapi import FastAPI, status, Response, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.websockets import WebSocket
from enum import Enum

from auth import authentication
from router import blog_get, blog_post, user, article, product, file, dependencies
from exceptions import StoryException
from db import models
from db.database import engine
from client import user_chat

app = FastAPI()
app.include_router(file.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(authentication.router)
app.include_router(dependencies.router)

@app.get('/')
async def chat():
  return HTMLResponse(user_chat)

clientes = []

@app.websocket('/chat')
async def chat_response(websocket: WebSocket):
  await websocket.accept()
  clientes.append(websocket)

  while True:
    data = await websocket.receive_text()
    for client in clientes:
      await client.send_text(data)


@app.get('/alive')
def alive():
  return {'message', 'Hello World'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
  return JSONResponse(
    status_code = 418,
    content = {'detail': exc.descritpion}
  )

# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#   return PlainTextResponse(str(exc), status_code=400)
models.Base.metadata.create_all(engine)

@app.middleware("http")
async def add_middleware(request: Request, call_next):
  start_time = time.time()
  response = await call_next(request)
  duration = time.time() - start_time

  response.headers['duration'] = str(duration)

  return response

origins = [
  '*'
]

app.add_middleware(
  CORSMiddleware, 
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ['*'],
  allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory='files'), name='files')



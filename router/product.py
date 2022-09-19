from typing import Optional, List
from fastapi import APIRouter, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse

router = APIRouter(
  prefix='/products',
  tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.get('/')
def get_all_products():
  data = ' '.join(products)
  response = Response(content=data, media_type='text/plain')

  response.set_cookie(key = 'test_cookie', value='test_cookie_value')

  return response

@router.get('/withheader')
def get_products(
  response: Response, 
  custom_header: Optional[List[str]] = Header(None),
  test_cookie: Optional[str] = Cookie(None)
):
  if custom_header:
    headers = ' and '.join(custom_header)
    response.headers['custom-reponse-headers'] = headers

  return {
    'data': products,
    'custom_header': custom_header,
    'my_cookie': test_cookie
  }

@router.get('/{id}', responses = {
  200: {
    "content": {
      "text/html": {
        "Product"
      }
    }
  },
  404: {
    "content": {
      "text/plain": {
        "Product not available"
      }
    },
    "description": "A cleartext error message"
  }
})

def get_product(id: int):
  if id > len(products):
    out = "Product not available"
    return PlainTextResponse(content=out, status_code=404, media_type="text/plain")
  
  product = products[id]

  out = f"""
    <html> 
      <head>
        <style>
          .product {{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            text-align: center;
          }}
        </style>
      </head>
      <body>
        <div class="product">{product}</div>
      </body>
    </html>
  """

  return HTMLResponse(content=out, media_type="text/html")

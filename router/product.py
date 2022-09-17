from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, PlainTextResponse

router = APIRouter(
  prefix='/products',
  tags=['product']
)

products = ['watch', 'camera', 'phone']

@router.get('/')
def get_all_products():
  data = ' '.join(products)
  return Response(content=data, media_type='text/plain')

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

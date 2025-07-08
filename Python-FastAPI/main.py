from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello from FastAPI'}

# dynamic route (path parameter)
@app.get('/hello/{name}')
def say_hello(name: str):
    return {'messagge': f'Hello, {name}'}


# POST requests with JSON input
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + (item.tax or 0)
    return {"name": item.name, "total_price": total_price}
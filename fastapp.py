from fastapi import FastAPI
from pydantic import BaseModel
from src.cat import Cat

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
def create_item(item: Item):
    """ Create an item with all the information: 
    - name: str
    - description: str
    - price: float
    - tax: float
    """
    return item

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/cat")
def cat():
    cat = Cat("Bob")
    return {"message": cat.speak()}

# Dynamic endpoint
@app.get("/cat/{name}")
def cat_name(name: str):
    cat = Cat(name)
    return {"name": name, "message": cat.speak()}

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/add")
def add(x: int, y: int,z:str):
    print("x=",type(x))
    print("z=",type(z))
    return {"result": x + y}

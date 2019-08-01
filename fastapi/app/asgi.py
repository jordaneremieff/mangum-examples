from mangum import Mangum
from fastapi import FastAPI


app = FastAPI()


@app.post("/items/")
def create_item(item_id: int):
    return {"id": item_id}


@app.get("/items/")
def list_items():
    items = [{"id": i} for i in range(10)]
    return items


@app.get("/")
def read_root():
    return {"Hello": "World!"}


handler = Mangum(app)

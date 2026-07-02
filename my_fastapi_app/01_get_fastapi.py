# 1. The GET Operation: Retrieving Data

# The GET method is used to request data from a specified resource. It is the most common HTTP method and is considered 'safe' and 'idempotent.' 'Safe' means it should not alter the state of the server (it only retrieves data), and 'idempotent' means making the same GET request multiple times should have the same effect as making it once (it will not change the data).

# Why is GET important?

# Data Retrieval: It's the primary way clients fetch information from your API. Examples include fetching a list of users, retrieving details of a specific product, or getting the current weather data.
# Read-Only Operations: It ensures that your data retrieval operations do not accidentally modify server-side data.
# Caching: GET requests can be cached by browsers and intermediate proxies, improving performance.
# How to implement GET in FastAPI:

# You use the @app.get('/') decorator, where app is your FastAPI instance and '/' is the path. The function decorated will be executed when a GET request is made to that path.

# Example:


from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Welcome to the API!"}



fake_items_db = {
    1: {"name": "Foo", "price": 50.2}
}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        return {"error": "Item not found"}
    fake_items_db[item_id] = item.dict()
    return {"item_id": int, **item.dict()}

# Using the same fake_items_db from the PUT example
fake_items_db = {
    1: {"name": "Foo", "price": 50.2}
}

@app.delete('/items/{item_id}')
def delete_item(item_id: int):
    if item_id not in fake_items_db:
        return {"error": "Item not found"}
    del fake_items_db[item_id]
    return {"message": f"Item {item_id} deleted successfully"}



#here I havecombined the PUT AND DELETE WITH GET operation to show how they can work together in a FastAPI application. The GET operation retrieves data, while the PUT operation updates existing data, and the DELETE operation removes data. This combination allows for a complete CRUD (Create, Read, Update, Delete) functionality in your API.

# 3. The PUT Operation: Updating Existing Resources

# The PUT method is used to update an existing resource or, if the resource does not exist, to create it. PUT requests are idempotent. This means that sending the same PUT request multiple times will have the same effect as sending it once. If you PUT the same data to the same resource multiple times, the resource will end up in the same state as if you had sent it just once.

# Why is PUT important?

# Full Resource Updates: It's typically used for replacing an entire resource with new data. If you only want to update a few fields, PATCH is often preferred, though PUT can be used for partial updates if the server logic handles it that way.
# Idempotency: Its idempotent nature makes it predictable for updates.
# How to implement PUT in FastAPI:

# You use the @app.put('/') decorator. Similar to POST, it often receives data in the request body.

# Example:

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# In-memory storage for demonstration
fake_items_db = {
    1: {"name": "Foo", "price": 50.2}
}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        return {"error": "Item not found"}
    fake_items_db[item_id] = item.dict()
    return {"item_id": int, **item.dict()}


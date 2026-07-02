# 2. The POST Operation: Creating New Resources

# The POST method is used to submit data to be processed to a specified resource. This often results in a change in state or side effects on the server. Unlike GET, POST requests are not necessarily safe or idempotent. Sending the same POST request twice might create two identical resources.

# Why is POST important?

# Resource Creation: It's the standard way to create new resources. For example, creating a new user account, adding a new product to an inventory, or submitting a new comment on a blog post.
# Sending Complex Data: It's used when you need to send a significant amount of data in the request body, such as form submissions or JSON payloads.
# How to implement POST in FastAPI:

# You use the @app.post('/') decorator. The data sent in the request body will typically be parsed into a Python object, often using Pydantic models for validation.

# Example:

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

@app.post('/items/')
def create_item(item: Item):
    return item
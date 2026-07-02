# Example 1: Creating a New Item

# Let's define a model for an item and create a POST endpoint to add new items.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 1. Define the Pydantic Model
class Item(BaseModel):
    name: str
    description: Optional[str] = None  # Optional field with a default value of None
    price: float
    tax: Optional[float] = None

# Simulate an in-memory database
fake_items_db = {}
item_id_counter = 1

# 2. Create a POST endpoint using the model
@app.post('/items/')
def create_item(item: Item):
    global item_id_counter
    item_data = item.dict() # Convert Pydantic model to dictionary
    
    # Add the item to our 'database'
    fake_items_db[item_id_counter] = item_data
    
    response_data = {
        "id": item_id_counter,
        **item_data  # Unpack the item data into the response
    }
    
    item_id_counter += 1
    return response_data
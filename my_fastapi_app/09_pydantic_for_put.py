# Example 2: Updating an Item with PUT

# Let's adapt the Pydantic model for a PUT request to update an existing item.

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

# Simulate an in-memory database
fake_items_db = {
    1: {"name": "Laptop", "description": "A powerful computing device", "price": 1200.50, "tax": 50.00}
}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item_id not in fake_items_db:
        return {"error": "Item not found"}
        
    # Update the item in the 'database'
    fake_items_db[item_id] = item.dict()
    
    return {
        "id": item_id,
        **item.dict()
    }
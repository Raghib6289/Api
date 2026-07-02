# . The DELETE Operation: Removing Resources

# The DELETE method is used to delete a specified resource. Like GET, DELETE requests are generally considered safe and idempotent. Deleting a resource multiple times should ideally result in the same state (the resource is gone).

# Why is DELETE important?

# Resource Removal: It's the standard way to remove data from your API.
# Data Management: Essential for maintaining data integrity and managing resources that are no longer needed.
# How to implement DELETE in FastAPI:

# You use the @app.delete('/') decorator. Typically, the identifier of the resource to be deleted is passed via the path.

# Example:

from fastapi import FastAPI

app = FastAPI()

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
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/items/{item_name}')
# def get_item(item_name: str):
#     return {"item_name": item_name, "message": f"You requested item: {item_name}"}


# Handling Multiple Path Parameters:

# You can define multiple path parameters in a single path.

# While path parameters are excellent for identifying specific resources, query parameters are used to filter, sort, or paginate collections of resources. They appear in the URL after a question mark (?) and are typically key-value pairs separated by ampersands (&). For example: /items?skip=0&limit=10.

from fastapi import FastAPI

app = FastAPI()

# Simulate a list of items
fake_items = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Orange", "price": 0.6},
    {"id": 4, "name": "Grapes", "price": 2.0},
    {"id": 5, "name": "Mango", "price": 1.5},
    {"id": 6, "name": "Pineapple", "price": 3.0}
]

@app.get('/items/')
def read_items(skip: int = 0, limit: int = 10):
    # Basic validation for limit
    if limit > 100:
        limit = 100
    
    paginated_items = fake_items[skip : skip + limit]
    return {
        "total_items": len(fake_items),
        "items_returned": len(paginated_items),
        "data": paginated_items
    }



# Testing this endpoint:

# Default behavior: Navigate to http://127.0.0.1:8000/items/. You'll get the first 10 items (since skip=0 and limit=10 are defaults).
# With query parameters: Navigate to http://127.0.0.1:8000/items/?skip=2&limit=3. This will return items starting from index 2, for a total of 3 items.
# Invalid limit: Navigate to http://127.0.0.1:8000/items/?limit=200. Due to our server-side logic, it will cap the limit at 100.
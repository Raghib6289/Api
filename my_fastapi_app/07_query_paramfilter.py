# Example 2: Query Parameters for Filtering

# Let's add a filter for item price.

from fastapi import FastAPI

app = FastAPI()

fake_items = [
    {"id": 1, "name": "Apple", "price": 0.5},
    {"id": 2, "name": "Banana", "price": 0.3},
    {"id": 3, "name": "Orange", "price": 0.6},
    {"id": 4, "name": "Grapes", "price": 2.0},
    {"id": 5, "name": "Mango", "price": 1.5},
    {"id": 6, "name": "Pineapple", "price": 3.0}
]

@app.get('/items/')
def read_items(
    skip: int = 0,
    limit: int = 10,
    min_price: float | None = None  # Optional minimum price filter
):
    paginated_items = fake_items[skip : skip + limit]
    
    # Apply price filter if provided
    if min_price is not None:
        paginated_items = [item for item in paginated_items if item["price"] >= min_price]
        
    return {
        "total_items": len(fake_items),
        "items_returned": len(paginated_items),
        "data": paginated_items
    }


# Testing this endpoint:

# http://127.0.0.1:8000/items/?min_price=1.0: This will return items with a price of 1.0 or higher.
# http://127.0.0.1:8000/items/?skip=1&limit=3&min_price=0.5: This combines pagination and filtering.
# Path parameters are a powerful feature that allows you to create dynamic URLs for your API endpoints. Instead of having static paths like /users/123, you can define a path parameter like /users/{user_id}, where {user_id} acts as a placeholder. FastAPI then extracts the value from the URL and passes it as an argument to your Python function.


# Example 1: Retrieving a Specific User

# Let's create an endpoint to get a user's details based on their ID.


from fastapi import FastAPI

app = FastAPI()

# Simulate a database of users
fake_users_db = {
    1: {"username": "alice", "email": "alice@example.com"},
    2: {"username": "bob", "email": "bob@example.com"}
}

@app.get('/users/{user_id}')
def get_user(user_id: int):
    if user_id in fake_users_db:
        return fake_users_db[user_id]
    else:
        return {"error": "User not found"}

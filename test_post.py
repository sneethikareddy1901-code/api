import post
from post import User

# Directly call the route handler functions instead of making HTTP requests.

def test_home():
    assert post.home() == {"message": "hello world"}

def test_hello():
    assert post.hello("Aj") == {"message": "hello Aj "}

def test_create_user():
    user = User(name="Bob", age=30)
    assert post.create_user(user) == {"message": " Hello Bob ", "age": 30}

if __name__ == "__main__":
    test_home()
    test_hello()
    test_create_user()
    print("All tests passed.")

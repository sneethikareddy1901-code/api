sfrom fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

@app.get("/")
def home():
    return{"message":"hello world"}

@app.get("/hello")
def hello(name:str):
    return{"message":f"hello {name} "}


@app.post("/user")
def create_user(user: User):
    return{
           "message" : f" Hello {user.name }",
	   "age": user.age
}


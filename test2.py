from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    name:str
    age:int


@app.get("/")
def snee():
    return {"message": "Sneethika is a good girl"}

@app.post("/he")
def vii(user:User):
    return {"message": f"Hello {user.name}",
             "age": user.age }

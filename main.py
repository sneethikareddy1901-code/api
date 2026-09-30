from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name:str
    age:int


@app.get("/gang")
def gang():
    return{"message":"hii {name}"}

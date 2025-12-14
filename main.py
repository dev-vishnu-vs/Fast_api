from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class   post(BaseModel):
    title: str
    content: str
    published:bool = True
    rating:Optional[int] = None



@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/posts")
def posts():
    return {"data": "this is your posts "}

#post method url : "/data"

@app.post("/createposts")
def create_posts(new_post:post ):
    print(new_post)
    print(new_post.dict())
    return {"data": new_post}

#title str, content str


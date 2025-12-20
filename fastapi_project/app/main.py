from http.client import responses
from typing import Optional,List

from django.forms.widgets import Select
from fastapi import FastAPI, Response,status,HTTPException,Depends
from fastapi.params import Body
from pydantic import BaseModel

from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models, schemas,utils
from .database import engine,get_db
from .router import post,user



models.Base.metadata.create_all(bind=engine)

app = FastAPI()



while True:
    try:
        conn = psycopg2.connect(host='localhost',
                                database='fastapi',
                                user='postgres',
                                password='malayali@2025',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break

    except Exception as error:
        print("Connecting to database failed")
        print("error", error)
        time.sleep(2)

my_posts = [{
    "title": "title of post 1","content": "content of the post 1", "id": 1},

    {"title": "favorite foods" ,"content":"I like pizza", "id":2 }]

def find_post(id):
    for post in my_posts:
        if post["id"] == id:
            return post

def find_index(id: int):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Hello world"}




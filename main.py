from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}

@app.get("/posts")
def posts():
    return {"data": "this is your post data"}





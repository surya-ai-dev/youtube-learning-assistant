from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    
    
    return {"message": "YouTube Learning Assistant API"}


@app.get("/home")
def home():
    return {"message": "I am in home"}
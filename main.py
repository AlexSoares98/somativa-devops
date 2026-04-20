from random import randint
from fastapi import FastAPI
import random

app = FastAPI()

# http://127.0.0.1:8000
@app.get("/")
async def root():
    return {"message": "Hello World"}

# http://127.0.0.1:8000/teste1
@app.get("/teste1")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,1000)}

@app.get("/status")
async def status():
    return {"status": "Ok"}
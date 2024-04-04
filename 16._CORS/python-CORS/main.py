from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/timestamp")
def timestamp():
    return { "time": datetime.now() }


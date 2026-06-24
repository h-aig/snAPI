import requests
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # customize this to only allow certain domains!
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hn")
def get_hn_data():
    """Get a hacker news story.""" # this is a docstring
    return  {requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').text}

uvicorn.run(app)
import os

from api import json_response
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from mongoengine import connect
from views import browse

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(browse.router)
app.include_router(json_response.router)


@app.on_event("startup")
async def startup_event():
    connect(alias="core", host=os.environ.get("MONGODB_URL"))

import itertools

from fastapi import FastAPI

from app.api.v1.endpoints import items, users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

def test_root():
    return {"message": "Welcome to the FastAPI application!"}
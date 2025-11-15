"""
Main application file for the Asset Tracker API.
"""
from fastapi import FastAPI
from database import Base, engine
from models import asset_model

app = FastAPI(title="Asset Tracker API", version="1.0.0")

@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the Asset Tracker API"}

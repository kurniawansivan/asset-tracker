"""
Main application file for the Asset Tracker API.
"""
from fastapi import FastAPI
from routers import asset_router

app = FastAPI(title="Asset Tracker API", version="1.0.0")

app.include_router(asset_router.router)

@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the Asset Tracker API"}

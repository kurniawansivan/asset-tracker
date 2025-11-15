"""
Main application file for the Asset Tracker API.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import asset_router, user_router

app = FastAPI(title="Asset Tracker API", version="1.0.0")

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(asset_router.router)
app.include_router(user_router.router)

@app.get("/")
def read_root():
    """Root endpoint returning a welcome message."""
    return {"message": "Welcome to the Asset Tracker API"}

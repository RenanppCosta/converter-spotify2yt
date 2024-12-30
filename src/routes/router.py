from fastapi import FastAPI
from src.routes import playlist

def config_routes(app: FastAPI):
    app.include_router(playlist.router)
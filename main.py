from fastapi import FastAPI
from src.routes.router import config_routes

def create_app():
    app = FastAPI()

    config_routes(app)
    
    return app

app = create_app()
from fastapi import APIRouter
from src.services.scraper import scrape_playlist_spotify

router = APIRouter()

@router.get("/")
async def home():

    list_music = scrape_playlist_spotify()
    return {"list": len(list_music)}
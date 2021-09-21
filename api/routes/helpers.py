from fastapi import APIRouter
from api import __version__

router = APIRouter()


@router.get("/")
async def update_admin():
    return {"message": "ping"}


@router.get("/version")
async def update_admin():
    return {"version": __version__}

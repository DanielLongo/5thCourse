from app.models import User
from app.dependencies import (
    get_user_from_access_token,
)
from fastapi import APIRouter, Depends, Body

router = APIRouter()

@router.post("/uploadPreferences")
async def upload_preferences(
    user: User = Depends(get_user_from_access_token),
    preferences: dict = Body(...),
):

    user.preferences = preferences
    user.save()
    return {"success": True}


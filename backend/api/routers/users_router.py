from typing import Dict

from fastapi import APIRouter, Depends
from fastapi.security import APIKeyCookie
from ..dependencies.db import get_db
from ..dependencies.auth import validate_cookie_session
from sqlalchemy.orm import Session
from ..schemas.user_schemas import User, FirebaseUser
from ..services.users_service import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

fake_items_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

cookie_scheme = APIKeyCookie(name="__session")


@router.get("/", response_model=list[User], dependencies=[Depends(validate_cookie_session), Depends(cookie_scheme)])
async def list_users(
        db: Session = Depends(get_db),
):
    users_service = UsersService(db)
    users = users_service.get_users()
    return users


from fastapi import APIRouter, Depends
from fastapi.security import APIKeyCookie
from api.dependencies.db import get_db
from sqlalchemy.orm import Session
from api.domain.users.user_schemas import User
from api.domain.users.users_service import UsersService

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

cookie_scheme = APIKeyCookie(name="__session")


@router.get("/", response_model=list[User])
async def list_users(
        db: Session = Depends(get_db),
):
    users_service = UsersService(db)
    users = users_service.get_users()
    return users

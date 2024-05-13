
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from ..dependencies.auth import get_firebase_user
from ..schemas.user_schemas import UserRecord, UserCredentials, LoginResult
from ..dependencies.db import get_db
from sqlalchemy.orm import Session
from ..services.users_service import UsersService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

bearer_scheme = HTTPBearer()


@router.post("/signup/", response_model=UserRecord, dependencies=[Depends(bearer_scheme)])
async def signup(
        user: UserRecord = Depends(get_firebase_user),
        db: Session = Depends(get_db)
):
    users_service = UsersService(db=db)
    return users_service.create_user(user)


@router.post("/login/", response_model=LoginResult, dependencies=[Depends(bearer_scheme)])
async def login(
        response: Response,
        user: UserRecord = Depends(get_firebase_user),
        db: Session = Depends(get_db),
):
    users_service = UsersService(db=db)
    cookie_token = users_service.create_cookie_token(user)
    response.set_cookie(key="__session", value=cookie_token, max_age=7200, httponly=True)
    return {"token": cookie_token }


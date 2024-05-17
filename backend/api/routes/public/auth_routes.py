
from typing import Annotated

from fastapi import APIRouter, Depends, Response
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from api.domain.auth.auth_service import AuthService
from api.domain.auth.auth_schemas import AuthenticationCredentials, AuthenticationResponse
from api.dependencies.db import get_db
from api.domain.users.user_schemas import UserRecord
from api.domain.users.users_service import UsersService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
    responses={404: {"description": "Not found"}},
)

bearer_scheme = HTTPBearer()


@router.post("/signup/", response_model=UserRecord)
async def signup(
        data: AuthenticationCredentials,
        db: Session = Depends(get_db),
):
    user = AuthService.get_firebase_user(data.id_token)
    users_service = UsersService(db=db)
    return users_service.create_user(user)


@router.post("/login/", response_model=AuthenticationResponse)
async def login(
        response: Response,
        data: AuthenticationCredentials
):
    user = AuthService.get_firebase_user(data.id_token)
    cookie_token = AuthService.create_cookie_token(user)

    response.set_cookie(key="__session", value=cookie_token, max_age=7200, httponly=True)
    return {"token": cookie_token}

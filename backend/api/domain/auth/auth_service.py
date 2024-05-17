import logging

from jose import jwt
from fastapi import HTTPException
from api.domain.users.user_schemas import UserRecord
from firebase_admin import auth

from http.client import HTTPException


class AuthService:
    @staticmethod
    def get_firebase_user(id_token: str) -> UserRecord:
        if not id_token:
            raise HTTPException(status_code=400, detail='TokenID must be provided')

        try:
            claims = auth.verify_id_token(id_token.removeprefix('Bearer '))
            return UserRecord(uid=claims['uid'], email=claims['email'], email_verified=claims['email_verified'])
        except Exception as e:
            logging.exception(e)
            raise HTTPException(status_code=401)

    @staticmethod
    def create_cookie_token(user: UserRecord) -> str:
        return jwt.encode({
            "email": user.email,
            "uid": user.uid,
            "email_verified": user.email_verified
        }, "secret", algorithm="HS256")
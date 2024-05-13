"""Template App
"""
import logging

from fastapi import HTTPException
from starlette.requests import Request
from api.schemas.user_schemas import UserRecord
from firebase_admin import auth
from jose import jwt

def get_firebase_user(request: Request) -> UserRecord:
    """Get the user details from Firebase, based on TokenID in the request

    :param request: The HTTP request
    """
    id_token = request.headers.get('Authorization')
    if not id_token:
        raise HTTPException(status_code=400, detail='TokenID must be provided')

    try:
        claims = auth.verify_id_token(id_token.removeprefix('Bearer '))
        return UserRecord(uid=claims['uid'], email=claims['email'], email_verified=claims['email_verified'])
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=401, detail='Unauthorized')


def validate_cookie_session(request: Request) -> UserRecord:
    session_cookie = request.cookies.get('__session')
    if not session_cookie:
        raise HTTPException(status_code=401, detail='Unauthorized')

    try:
        decoded = jwt.decode(session_cookie, "secret", algorithms=["HS256"])
        return UserRecord(uid=decoded['uid'], email=decoded['email'], email_verified=decoded['email_verified'])
    except Exception as e:
        logging.exception(e)
        raise HTTPException(status_code=401, detail='Unauthorized')
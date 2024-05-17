"""Template App
"""
import logging

from jose import jwt
from fastapi import HTTPException
from starlette.requests import Request
from api.domain.users.user_schemas import UserRecord


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
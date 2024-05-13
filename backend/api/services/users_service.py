from jose import jwt
from firebase_admin.auth import create_user, get_user, get_user_by_email, EmailAlreadyExistsError, verify_id_token
from fastapi import HTTPException
from api.models.user_model import User
from api.schemas.user_schemas import UserCredentials, UserRecord
from sqlalchemy.orm import Session


class UsersService:
    def __init__(self, db: Session):
        self.db = db

    def get_users(self):
        return self.db.query(User).all()

    def get_user(self, uid: str) -> UserRecord:
        return get_user(uid=uid)

    def get_user_by_email(self, email):
        return get_user_by_email(email=email)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            raise Exception("User not found")
        user.name = data["name"]
        user.save()
        return user

    def get_or_create_user_in_db(self, uid: str, email: str) -> UserRecord:
        user = self.db.query(User).filter_by(id=uid).first()
        if not user:
            user = User(id=uid, email=email)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        return user

    def create_user(self, user: UserRecord) -> UserRecord:
        self.get_or_create_user_in_db(user.uid, user.email)
        return user

    def create_cookie_token(self, user: UserRecord) -> str:
        return jwt.encode({
            "email": user.email,
            "uid": user.uid,
            "email_verified": user.email_verified
        }, "secret", algorithm="HS256")

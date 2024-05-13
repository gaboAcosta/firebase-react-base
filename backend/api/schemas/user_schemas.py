from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class FirebaseUser(BaseModel):
    email_verified: bool
    user_id: str


class UserCredentials(UserBase):
    password: str


class User(UserBase):
    id: str

    class Config:
        from_attributes = True


class UserRecord(BaseModel):
    uid: str
    email: str
    email_verified: bool


class LoginResult(BaseModel):
    token: str

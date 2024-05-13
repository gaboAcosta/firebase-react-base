from pydantic import BaseModel


class AuthenticationCredentials(BaseModel):
    email: str
    password: str

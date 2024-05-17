from pydantic import BaseModel


class AuthenticationCredentials(BaseModel):
    id_token: str


class AuthenticationResponse(BaseModel):
    token: str

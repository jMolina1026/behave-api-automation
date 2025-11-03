from pydantic import ValidationError, BaseModel


class RegisterUser(BaseModel):
    id: int
    token: str


class RegisterUserUnsuccessful(BaseModel):
    error: str
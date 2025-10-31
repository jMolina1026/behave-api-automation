from pydantic import ValidationError, BaseModel


class RegisterUser(BaseModel):
    id: int
    token: str
from pydantic import BaseModel

class UpdateUserSchema(BaseModel):
    name: str
    job: str
    updatedAt: str

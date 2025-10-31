from pydantic import BaseModel

class UpdateUserPatchSchema(BaseModel):
    name: str
    job: str
    updatedAt: str

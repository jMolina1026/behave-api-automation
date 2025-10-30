from typing import List, Dict

from pydantic import BaseModel


class CreatedUser(BaseModel):
    id: int
    job: str
    name: str
    createdAt: str

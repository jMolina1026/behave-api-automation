from typing import List, Dict

from pydantic import BaseModel


class Data(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

class Support(BaseModel):
    url: str
    text: str


class Meta(BaseModel):
    powered_by: str
    upgrade_url: str
    docs_url: str
    template_gallery: str
    message: str
    features: List[str]
    upgrade_cta: str

class UsersSchema(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support
    _meta: Meta

class SingleUserSchema(BaseModel):
    data: Data
    support: Support
    _meta: Meta


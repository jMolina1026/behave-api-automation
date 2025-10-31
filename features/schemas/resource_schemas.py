from typing import List, Dict

from pydantic import BaseModel


class Data(BaseModel):
    id: int
    name: str
    year: int
    color: str
    pantone_value: str

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

class ResourcesSchema(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[Data]
    support: Support
    _meta: Meta

class SingleResourceResponse(BaseModel):
    data: Data
    support: Support
    _meta: Meta

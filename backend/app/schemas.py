from pydantic import BaseModel


class PaperCreate(BaseModel):
    title: str
    year: int
    author: str


class RelationshipCreate(BaseModel):
    source_id: str
    target_id: str
    relation_type: str
import datetime
from pydantic import BaseModel


class JobCreate(BaseModel):
    subject: str
    content: str


class JobResponse(BaseModel):
    id: int
    content: str
    subject: str
    create_date: datetime.datetime

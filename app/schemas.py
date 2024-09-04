from pydantic import BaseModel, Field


class APICreateRequest(BaseModel):
    telefon: str

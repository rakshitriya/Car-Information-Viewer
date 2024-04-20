from pydantic import BaseModel, Field
from typing import Optional, List

class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(ge=1970, lt=2024)
    price: Optional[float]
    engine: Optional[str] = "V4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]
    
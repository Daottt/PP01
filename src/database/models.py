from typing import Optional
from pydantic import BaseModel

class BaseModelModify(BaseModel):
    id: Optional[int] = None

class Users(BaseModelModify):
    login: str
    password: str
    power_level: Optional[int] = None

class Requests(BaseModelModify):
    add_date: Optional[str] = None
    animal_id: Optional[int]
    user_id: Optional[int] = None
    treatment_type: Optional[str] = None
    disease_id: Optional[int] = None
    treatment_status: Optional[str] = None
    end_date: Optional[str] = None

class Animals(BaseModelModify):
    name: Optional[str] = None

class Diseases(BaseModelModify):
    name: Optional[str] = None

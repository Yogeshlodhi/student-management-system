from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class StudentResponse(BaseModel):
    name: str
    age: int

class StudentListResponse(BaseModel):
    data: List[StudentResponse]
    
class Student(BaseModel):
    # id: str
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None

class StudentResponse(BaseModel):
    id: str = Field(..., alias = "id")
    name: str
    age: int
    address: Address
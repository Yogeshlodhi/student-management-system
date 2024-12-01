from fastapi import APIRouter, HTTPException, Query, Path, Depends
from app.crud import create_student, list_students, fetch_student, update_student, delete_student

from app.models import Student, UpdateStudent, StudentResponse, StudentListResponse
from app.db import db 

from bson import ObjectId, errors

router = APIRouter(prefix="/students", tags=["Students"])

def is_valid_object_id(id: str) -> bool:
    try:
        ObjectId(id)
        return True
    except errors.InvalidId:
        return False


@router.post("/", response_model=dict, status_code=201)
async def add_student(student: Student):
    try:
        student_id = await create_student(db, student.dict())
        return {"id": student_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=StudentListResponse)
async def get_students(country: str = Query(None), age: int = Query(None)):
    filters = {}
    if country:
        filters["address.country"] = country
    if age is not None:
        filters["age"] = {"$gte": age}

    students = await list_students(db, filters)
    return students

@router.get("/{id}", response_model=Student)
async def get_student_by_id(id: str = Path(...)):
    if not is_valid_object_id(id):
        raise HTTPException(status_code=400, detail="Invalid student ID format")
    student = await fetch_student(db, id)
    if not student:
        raise HTTPException(status_code=404, detail= "Student not found")
    return student

@router.patch("/{id}", status_code=204)
async def update_student_by_id(id: str, updates: UpdateStudent):
    if not await update_student(db, id, updates.dict(exclude_unset=True)):
        raise HTTPException(status_code=404, detail= "Student not found or no updates were made")
    # return {"message": "Student updated successfully"}

@router.delete("/{id}", status_code=200)
async def delete_student_by_id(id: str):
    if not await delete_student(db, id):
        raise HTTPException(status_code=404, detail="Student not found")
    # return {"message": "Student deleted successfully"}
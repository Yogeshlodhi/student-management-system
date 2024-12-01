from bson import ObjectId
from pymongo.errors import DuplicateKeyError

def student_helper(student) -> dict:
    return {
        "_id": str(student["_id"]),
        "name": student["name"],
        "age": student["age"],
        "address": student["address"],
    }

async def create_student(db, student: dict) -> str:
    try:
        result = await db.students.insert_one(student)
        return str(result.inserted_id)
    except DuplicateKeyError:
        raise ValueError("Student with this information already exists.")

async def list_students(db, filters: dict) -> dict:
    students_cursor = db.students.find(filters)
    students_list = []
    
    async for student in students_cursor:
        students_list.append({"name": student["name"], "age": student["age"]})
    
    return {"data": students_list}

async def fetch_student(db, student_id: str) -> dict:
    student = await db.students.find_one({"_id": ObjectId(student_id)})
    if student:
        return student_helper(student)
    return None

async def update_student(db, student_id: str, updates: dict) -> bool:
    result = await db.students.update_one({"_id": ObjectId(student_id)}, {"$set": updates})
    return result.modified_count > 0

async def delete_student(db, student_id: str) -> bool:
    result = await db.students.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0
# from fastapi import FastAPI
# from routers import student

# app = FastAPI(
#     title="Student Management System",
#     description="Manage students with FastAPI and MongoDB",
#     version="1.0.0"
# )

# app.include_router(student.router)

from fastapi import FastAPI
from app.routers import student  

app = FastAPI(
    title="Student Management System",
    description="Manage students with FastAPI and MongoDB",
    version="1.0.0"
)

app.include_router(student.router)


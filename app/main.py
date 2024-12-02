from fastapi import FastAPI
from app.routers import student
import os
import uvicorn

app = FastAPI(
    title="Student Management System",
    description="Manage students with FastAPI and MongoDB",
    version="1.0.0"
)

app.include_router(student.router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


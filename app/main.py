from fastapi import FastAPI
from app.routers import student
import os
import uvicorn

# Define the FastAPI application
app = FastAPI(
    title="Student Management System",
    description="Manage students with FastAPI and MongoDB",
    version="1.0.0"
)

# Include the router
app.include_router(student.router)

# Run the application using Uvicorn when executed as the main script
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)


# from fastapi import FastAPI
# from app.routers import student  

# import os
# import uvicorn

# if __name__ == "__main__":
#     port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
#     uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)

# app = FastAPI(
#     title="Student Management System",
#     description="Manage students with FastAPI and MongoDB",
#     version="1.0.0"
# )

# app.include_router(student.router)


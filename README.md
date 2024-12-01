[text](https://student-management-system-qn67.onrender.com)

# Student Management System API

## Description
The **Student Management System API** is a backend system built with FastAPI that is helpful to manage student's profile data.


## Features
- **Create Student**: Add a new student to the database.
- **Get Student by ID**: Retrieve detailed information about a specific student.
- **Update Student**: Modify the information of an existing student.
- **Delete Student**: Remove a student from the database.
- **List All Students**: Retrieve a list of all students.

## Tech Stack
- **Framework**: FastAPI
- **Database**: MongoDB
- **Language**: Python
- **Tools**: 
  - AsyncIO for non-blocking operations.
  - Uvicorn as the ASGI server.

## Installation

### Prerequisites
- Python 3.8+
- MongoDB (or any database supported by your app)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Yogeshlodhi/student-management-system
   cd student-management-system

2. Create a virtual environment
    ```bash
    python -m venv myenv

3. Activate the virtual environment
    ```bash
    .\myenv\Scripts\activate

4. Install all the required dependencies/modules
  ```bash
  pip install -r requirements.txt

5. Test the server 
  ```bash
  uvicorn app.main:app --reload

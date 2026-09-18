from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime import timedelta
from  auth.security import hash_password
from crud.students import student_crud
from crud.students.student_crud import get_student_by_email
from auth.security import verify_password,create_access_token
from schemas.student_schemas import StudentCreate

def register_new_student(db:Session,student_in:StudentCreate):
    if student_crud.get_student_by_email(db,email = student_in.email):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail="A student with this email already exists" 
        )
    if student_crud.get_teacher_by_username(db,username = student_in.username):
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= "A teacher with this username already exists"
        )

    hash_password =  hash_password(student_in.password)
    
    return student_in.create_teacher(
        db = db,
        username = student_in.username,
        email = student_in.email,
        hash_password = hash_password
    )
from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime import timedelta 
from  auth.security import  hash_password
from  crud import teacher as teacher_crud
from  crud import logging_teacher 
from model import Teachers
from schemas.teacher import TeacherCreate,Login


def register_new_teacher(db:Session,teacher_in:TeacherCreate):
    if teacher_crud.get_teacher_by_email(db,email = teacher_in.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= "A teacher with this email already exist."
        )
    
    if teacher_crud.get_teacher_by_username(db,username = teacher_in.username):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "A  teacher with this username already exists"
             
        )
        
    hashed_password = hash_password(teacher_in.password)
    
    return teacher_crud.create_teacher(
        db=db,
        username=teacher_in.username,
        email = teacher_in.email,
        hashed_password = hashed_password
    )
    
def log_teacher_in(db:Session,teacher_log:Login):
    if logging_teacher(db)
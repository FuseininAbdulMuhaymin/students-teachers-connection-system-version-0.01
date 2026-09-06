from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime import timedelta 
from  auth.security import  hash_password
from  crud import teacher as teacher_crud
from  crud import logging_teacher 
from models import Teachers
from schemas.teacher import TeacherCreate,Login
from crud import get_teacher_by_email
from auth import verify_password, create_access_token

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
    
def login_teacher(db: Session, email: str, password: str):

    # 1. Find teacher
    teacher = get_teacher_by_email(db=db,email=email)

    # 2. Check if teacher exists
    if not teacher:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")

    # 3. Verify password
    password_is_valid = verify_password(password,teacher.hashed_password)

    if not password_is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # 4. Create JWT
    access_token = create_access_token(
        data={"sub": str(teacher.id)}
    )

    # 5. Return token
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
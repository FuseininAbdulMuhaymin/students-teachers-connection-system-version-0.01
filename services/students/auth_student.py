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

    hashed_password =  hash_password(student_in.password)
    
    return student_in.create_teacher(
        db = db,
        username = student_in.username,
        email = student_in.email,
        hash_password = hash_password
    )
    
def login_teacher(db:Session,email:str,password:str):
    #Find the Student 
    student = get_student_by_email(db=db,email=email)
    
    #Check if teacher exists
    if not student:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid email or password")
    
    #Verify password
    password_is_valid = verify_password(password,student.hashed_password)
    
    if not password_is_valid:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password "
        )
    
    #4 Create JWT 
    access_token = create_access_token(
        data = {"sub":str(student.id)}

    )
    #5.Return  token .
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
          
          
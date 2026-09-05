from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime import timedelta 
from  auth.security import  hash_password
from  crud.teacher import teacher as teacher_crud
from models.teacher_model import Teachers
from schemas.teachers.teacher import TeacherCreate,Login,TokenResponse
from  auth.security import (
    DUMMY_HASH,
    create_access_token,
    verify_password,
)
from auth.security import get_setting
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
    

def authenticate_teacher(db:Session,email:str,password:str):
    teacher = teacher_crud.get_teacher_by_email(db,email=email)
    if not teacher:
        #it prevent timming attack
        verify_password(password,DUMMY_HASH)
        return False
    if not verify_password(password,teacher.hashed_password):
        return False
    return teacher

def login_teacher(db:Session,email:str,password:str)-> TokenResponse:
    teacher = authenticate_teacher(db=db,email=email,password=password)
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail= "Incorrect email or passwords",
            headers={"WWW-Authenticate":"Bearrer"}
        )
    settings = get_setting()
    acces_token_expire = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub":teacher.email},
        expires_delta=acces_token_expire,
    )
    
    return TokenResponse(access_token = access_token, token_type="bearrer")
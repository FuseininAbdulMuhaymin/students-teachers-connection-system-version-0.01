from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas.student_schemas import StudentCreate,StudentResponse,TokenResponse
from crud.students.student_crud import(
    create_student
)
from auth.security import hash_password
from services.students.auth_student import register_new_student
from typing import Annotated 
from fastapi.security import OAuth2PasswordRequestForm 
from services.students import auth_student as student_service

router = APIRouter(prefix="/students",tags=["Student"])

#Registering a student
@router.post("/",response_model=StudentCreate)
async def create_register_new_student(student_in:StudentCreate,db:Session = Depends(get_db)):
    return register_new_student(db=db,student_in=student_in)
        
@router.post("/auth/Login",response_model=TokenResponse)
async def login_for_access(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:Annotated[Session,Depends(get_db)]) -> TokenResponse:
    return student_service.login_teacher(
        db = db,
        email = form_data.username,
        passwored = form_data.password
    )
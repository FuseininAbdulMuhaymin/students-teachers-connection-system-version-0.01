from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from schemas.student_schemas import StudentCreate
from crud.students.student_crud import(
    create_student
)
from auth.security import hash_password
from services.students.auth_student import register_new_student
from typing import Annotated 
from fastapi.security import OAuth2PasswordRequestForm 
from services.students import auth_student

router = APIRouter(prefix="/students",tags=["Student"])

#Registering a student
@router.post("/",response_model=StudentCreate)
async def create_register_new_student(student_in:StudentCreate,db:Session = Depends(get_db)):
    return register_new_student(db=db,student_in=student_in,)
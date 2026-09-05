from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
# from typing import List
from schemas.teachers.teacher import TeacherCreate, TeacherReponse,TokenResponse,Login
from crud.teachers.teacher import(
    create_teacher,
    get_teacher,
    get_teachers,
    delete_teacher
)
from auth.security import hash_password
from services.teachers.auth_teacher import register_new_teacher
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from services import auth_teacher as teacher_service

router = APIRouter(prefix="/teachers",tags=["Teachers"])


##get all teachers
@router.get("/",response_model=TeacherReponse)
def read_teachers(db:Session=Depends(get_db)):
    return get_teachers(db)

##getting a teacher by Id
@router.get("/{teacher_id}",response_model=TeacherReponse)
def read_teacher(
    teacher_id:int,
    db:Session = Depends(get_db)
):
    return get_teacher(db,teacher_id)

#delete Teacher 
@router.delete("/{teacher_id}",response_model=TeacherReponse)
def remove_teacher(
    teacher_id:int,
    db:Session = Depends(get_db)
):
 
    return delete_teacher(db,teacher_id)

##Registing a user 
@router.post("/",response_model=TeacherCreate)
async def  create_register_teacher(teacher_in:TeacherCreate,db:Session = Depends(get_db)):
    return register_new_teacher(db=db,teacher_in = teacher_in)

#Loging Teacher 
@router.post("/auth/Login",response_model=TokenResponse)
async def login_for_access(form_data:Annotated[OAuth2PasswordRequestForm,Depends()],db:Annotated[Session,Depends(get_db)]) -> TokenResponse:
    return teacher_service.login_teacher(
        db = db,
        email= form_data.username,
        password = form_data.password
    )
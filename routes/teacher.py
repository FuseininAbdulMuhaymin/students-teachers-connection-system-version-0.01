from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from typing import List
from schemas.teacher import TeacherCreate, TeacherReponse
from crud.teacher import(
    create_teacher,
    get_teacher,
    get_teachers,
    delete_teacher
)
from auth.security import hash_password
from services.auth_teacher import register_teacher

router = APIRouter(prefix="/teachers",tags=["Teachers"])



    
    
#Teacher  Endpoint
# @router.post("/",response_model=TeacherReponse)
# def create_teacher(
#     teacher:TeacherCreate,
#     db:Session = Depends(get_db)
# ):
#     return  create_teacher(db,teacher)

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


#Registering a Teacher in 
@router.post("/register",response_model=TeacherReponse,status_code=status.HTTP_201_CREATED)
def register(teacher:TeacherCreate,db:Session=Depends(get_db)):
    
    return register_teacher(
        db=db,
        username=teacher.username,
        email=teacher.email,
        password=teacher.password
    )
    
#Logging a Teacher
@router.post("/Login",response_model=TeacherReponse,status_code=status.HTTP_201_CREATED)
def login_teacher(teacher:TeacherCreate,db:Session=Depends(get_db)):
    return login_teacher(
        email= teacher.email,
        password=teacher.password
    )
    
   
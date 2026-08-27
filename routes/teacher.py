from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
# from typing import List
from schemas.teacher import TeacherCreate, TeacherReponse,TokenResponse
from crud.teacher import(
    create_teacher,
    get_teacher,
    get_teachers,
    delete_teacher
)
from auth.security import hash_password
from services.auth_teacher import register_teacher,authentication_teacher

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

##Registing a user 
@router.post("/",response_model=TeacherCreate)
async def  register_teacher(teacher:TeacherCreate,db:Session = Depends(get_db)):
    return register_teacher(
    db=db,
    teacher = teacher
    )


    
# #Logging a Teacher
# @router.post("/login",response_model=TokenResponse)
# def login(credentials:TeacherCreate,db:Session = Depends(get_db)):
#    return authentication_teacher(
#        db=db,
#        username=credentials.username,
#        password=credentials.password
#    )
   
   
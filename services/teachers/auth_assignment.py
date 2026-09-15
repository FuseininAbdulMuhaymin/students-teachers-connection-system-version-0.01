from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime  import  datetime
from schemas.teachers.assignment import AssignmentCreate
from database import get_db
from crud.teachers.teacher import create_teacher
from fastapi.security import OAuth2PasswordRequestForm
from services.teachers.auth_teacher import login_teacher
from crud.teachers import assignment as assignment_crud
from crud.class_crud import class_crud
from utils.file_storage import save_assignment_file

async def create_assignment(db:Session,title:str,description:str,file_url:str,due_date:datetime,class_id:int,teacher_id:int,file):
    #1.checking if the class exists
    school_class = class_crud.get_class(db=db,class_id = class_id)
    
    if not school_class:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Class not found"
        )
        
    # #check if teacher teaches this class (But I thought this the  approach I want to use is different)
    # if school_class.teacher_id != teacher_id:
    #     raise HTTPException(
    #         status_code = status.HTTP_403_FORBIDDEN,
    #         detail="class not found"
    #     )
    
    #check due date
    if due_date <= datetime.now():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,detail="Due date must be in the future"
        )
    try:
        _,file_url = await save_assignment_file(file)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        )
        
    #call the Crud
    return assignment_crud.create_assignment(
        db = db,
        title=title,
        description=description,
        file_url=file_url,
        due_date=due_date,
        teacher_id=teacher_id,
        class_id=class_id,
         original_filename=file.filename
    )
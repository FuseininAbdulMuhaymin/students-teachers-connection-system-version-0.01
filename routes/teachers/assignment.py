from fastapi import APIRouter,Depends,HTTPException,status,Depends,Form,UploadFile,File
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from schemas.teachers.assignment import AssignmentCreate
from auth.security import authenticate_user
from datetime import datetime
from typing import Annotated
from services.teachers.auth_assignment import create_assignment



router = APIRouter(prefix="/teachers/Assginments",tags=["Asignments"])

#Creating Asssgnment
@router.post("/")
async def create_assignment_route(
    title: Annotated[str, Form()],
    description: Annotated[str, Form()],
    class_code: Annotated[int, Form()],
    due_date: Annotated[datetime, Form()],
    file: Annotated[UploadFile, File()],
    db: Session = Depends(get_db),
    current_teacher=Depends(authenticate_user),
):
    return await create_assignment(
        db=db,
        title=title,
        description=description,
        due_date=due_date,
        class_code=class_code,
        teacher_id=current_teacher.id,
        file=file,
    )

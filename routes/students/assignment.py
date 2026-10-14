from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from  typing import List
from schemas.student_schemas import  StudentCreate
from auth.security import authenticate_user
from datetime import datetime
from typing import Annotated

router = APIRouter(prefix="/student/Assignments",tags=["Assignment"])

#getting assignment from teachers 
@router.get("/")
async def create_assignment_route(db:Session,current_student = Depends(authenticate_user)):
    pass 
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from typing import List
from schemas.teachers.assignment import AssignmentCreate
from services.teachers.auth_teacher import login_teacher

router = APIRouter(prefix="/Assginment",tags=["Asignment"])

#Creating Asssgnment

@router.post("/",response_model=AssignmentCreate)
def create_Assignment(assign:AssignmentCreate,db:Session = Depends(login_teacher))):
    return assign


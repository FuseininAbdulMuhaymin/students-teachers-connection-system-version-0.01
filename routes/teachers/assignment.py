from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
import models
from typing import List
from schemas.teachers.assignment import AssignmentCreate


router = APIRouter(prefix="/Assginment",tags=["Asignment"])

#Creating Asssgnment

@router.post("/",response_model=AssignmentCreate)
def create_Assignment(assign:AssignmentCreate,db:Session = Depends(get_db)):
    return assign


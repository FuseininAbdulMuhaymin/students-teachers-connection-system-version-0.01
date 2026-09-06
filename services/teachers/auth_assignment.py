from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime  import  timedelta
from schemas.teachers.assignment import AssignmentCreate
from auth.dependencies import oauth2_scheme
from database import get_db
from crud.teachers.teacher import create_teacher

def create_assignment(db:Session,assign:AssignmentCreate):
    if  
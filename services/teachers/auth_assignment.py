from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from datetime  import  timedelta
from schemas.teachers.assignment import AssignmentCreate
from auth.dependencies import oauth2_scheme
from database import get_db
from crud.teachers.teacher impoart create_teacher
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from services import auth_teacher as teacher_service
from services.teachers.auth_teacher import login_teacher


def create_assignment(db:Session,assign:AssignmentCreate, get_db(Depends=(login_teacher))):
    
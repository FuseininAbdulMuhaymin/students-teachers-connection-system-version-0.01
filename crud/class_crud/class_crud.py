from sqlalchemy.orm import Session
from  models.teacher_model import Teachers
# from schemas.teacher import TeacherCreate
from fastapi import HTTPException,status
from database import get_db
from models.class_model import Class

#CREATING CLASS
def  get_class(db:Session,class_id:int):
    return(
      db.query(Class).filter(Class.id == class_id).first()
    )
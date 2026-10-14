from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from database import get_db
from models.class_model import Class

#CREATING CLASS
def  get_new_class(db:Session,class_code:int):
    return(
      db.query(Class).filter(Class.class_code == class_code).first()
    )
    
def create_new_class(db:Session,name:str,class_code:int):
  class__ = Class (
    name = name,
    class_code = class_code
  )
  
  
  db.add(class__)
  db.commit()
  db.refresh(class__)
  
  return class__
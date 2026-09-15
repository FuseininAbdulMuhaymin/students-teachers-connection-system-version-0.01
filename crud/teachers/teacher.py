from sqlalchemy.orm import Session
from  models.teacher_model import Teachers
# from schemas.teacher import TeacherCreate
from fastapi import HTTPException,status
from database import get_db

# #creating a teacher
# def create_teacher(db:Session,teacher:TeacherCreate):
#     db_teacher = Teachers(
#         username = teacher.username,
#         email=teacher.email,
#     )



#CREATING A TEACHER
#checking if username and email already exists 
def get_teacher_by_email(db:Session,email:str):
    return (db.query(Teachers).filter(Teachers.email==email).first())
def get_teacher_by_username(db:Session,username:str):
    return (db.query(Teachers).filter(Teachers.username == username).first())


def create_teacher(db:Session,username:str,email:str,hashed_password:str):
    teacher = Teachers(
        username = username,
        email = email,
        hashed_password = hashed_password
    )

    db.add(teacher)
    db.commit() 
    db.refresh(teacher)

    return teacher

   

#Logging Teacher 
#This is talking to  the database to checking
def get_teacher_email(db:Session,email:str):
    return db.query(Teachers).filter(Teachers.email==email).first()


    

# it job is only to 
# username
#    ↓
# database
#    ↓
# teacher / None


# GETTING ONE TEACHER
#getting  teacher by ID
def get_teacher(db:Session,teacher_id:int):
    teacher = db.query(Teachers)

#def get All  Teacher.It the same as select
def get_teachers(db:Session):
    return db.query(Teachers).all

#delete Teacher
def delete_teacher(db:Session,teacher_id:int):
    teacher= db.query(Teachers).filter(
        Teachers.id == teacher_id
    ).first()
    if not teacher:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    db.delete(teacher)
    db.commit()
    return teacher



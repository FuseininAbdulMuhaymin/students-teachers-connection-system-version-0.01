from sqlalchemy.orm import Session
from  model import Teachers
from schemas.teacher import TeacherCreate
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
    return(db.query(Teachers).filter(Teachers.email==email.first()))
def get_teacher_by_username(db:Session,username:str):
    return (db.query(Teachers).filter(Teachers.username == username).first())


def create_teacher(db:Session,username:str,email:str,hashed_password:str):
    teacher = Teachers(
        username = username,
        email = email,
        hashed_passsword = hashed_password
    )

    db.add(teacher)
    db.commit() 
    db.refresh(teacher)

    return teacher

# existing_email = email ==  query.first() .filter()
# if existing_email not in Session get_db:
#     def register_a_teacher(db:Session=Depends(get_db)):
#         username = username,
#         email = email,
#         password = password
# else:
#     raise HTTPException(status_code=status.201)

# existing_username = username query.first() .filter()
# if existing_username  not in Session  get_db:
#     def register_a_teacher(db:Session=Depends(get_db)):
#         username = username,
#         email = email,
#         password  = password
# else:
#     raise HTTPException(status_code=status.201)
 




#Logging Teacher 
#This is talking to  the database to chec
def get_teacher_by_username(db:Session,username:str):
    return(db.query(Teachers).filter(Teachers.username == username).first())    

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



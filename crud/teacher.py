from sqlalchemy.orm import Session
from  model import Teachers
from schemas.teacher import TeacherCreate
from fastapi import HTTPException,status

# #creating a teacher
# def create_teacher(db:Session,teacher:TeacherCreate):
#     db_teacher = Teachers(
#         username = teacher.username,
#         email=teacher.email,
#     )



#CREATING A TEACHER
#getting a teacher by email
def get_teacher_by_email(db:Session,email:str):
    db.query(Teachers).filter(Teachers.email == email).first()
    
# def get_teacher_by_username(db:Session,username:str):
#     db.query(Teachers).filter(Teachers.username == username).first()
         
#creating a teacher
def create_teacher(db:Session,teacher:TeacherCreate,password_hash:str):
    db_teacher= Teachers(
        username = teacher.username,
        email=teacher.email,
        password_hash=password_hash
    )

    # SAVING TO DATABASE
#Add to session:It prepare the object for insertion 
    db.add(db_teacher)
#committing : Save parmanently
    db.commit()
#Refresh:Fetch lastest value to postgresSQL
    db.refresh(db_teacher)
    return db_teacher


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

#def get All Teacher. it the same as select
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



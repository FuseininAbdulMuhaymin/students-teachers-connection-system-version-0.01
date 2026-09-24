from sqlalchemy.orm import Session
from models.student_model import Student
from fastapi import HTTPException,status
from database import get_db




#CREATING A TEACHER
#checking  if  username and email already exists
def  get_student_by_email(db:Session,email:str):
    return (db.query(Student).filter(Student.email == email).first())

def get_teacher_by_username(db:Session,username:str):
    return(db.query(Student).filter(Student.username == username).first())

def create_student(db:Session,username:str,password:str,email:str):
    student = Student(
        username = username,
        email = email,
        password = password,
    )
    
    db.add(student)
    db.commit()
    db.refresh(student)
    
    return student


#Loging Teacher
#This is talking  to the database to checking 
def get_student_email(db:Session,email:str):
    return db.query(Student).filter(Student.email == email).first()
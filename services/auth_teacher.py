from sqlalchemy.orm import Session
from auth.security import hash_password
from  crud.teacher import (create_teacher,get_teacher_by_email,get_teacher_username)
from fastapi import HTTPException, status
from auth.security import(verify_password,create_access_token)


#The Logic behind  Registering a Teacher
def register_teacher(db:Session,username:str,email:str,password:str,teacher):
    existing_email = get_teacher_by_email(db,email)
    if existing_email:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="Email alreaddy registered")
    #checking  username
    existing_username = get_teacher_username(db,username)
    if existing_username:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,details="Username already takenmko")


    hashed_password= hash_password(password)
    
     # Create teacher
    teacher = create_teacher(
        db=db,
        username=username,
        email=email,
        hashed_password=hashed_password
    )

    return teacher

#Loging  as teacher 
def logging_teacher(db:Session,username:str,email:str,password:str,teacher)
    existing_email = get_teacher_by_email(db,email)
    if email != existing_email:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
hashes_password = hash_password(password) 

teacher = create_teacher(
    db = db,
    username = username,
    email=email,
    hash_password = hash_password
)
 return teeacher
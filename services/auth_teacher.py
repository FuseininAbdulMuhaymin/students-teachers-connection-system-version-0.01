from sqlalchemy.orm import Session
from auth.security import hash_password
from  crud.teacher import (create_teacher,get_teacher_by_email,get_teacher_by_username)
from fastapi import HTTPException, status
from auth.security import(verify_password,create_access_token)


#The Logic behind  Registering a Teacher
def register_teacher(db:Session,username:str,email:str,password:str,teacher):
    existing_email = get_teacher_by_email(db,email)
    if existing_email:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="Email alreaddy registered")
    #checking_username
    existing_username = get_teacher_by_username(db,username)
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
def authentication_teacher(db:Session,username:str,password:str):
    #Find the teacher in the database
    teacher = get_teacher_by_username(db,username)
    
    #if the  teacher doesn't exists
    if not teacher:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid username or password")
    
    #check if the password provided is the  correct or 
    if not verify_password(password,teacher.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid pasword")
    
    #Create jwt after successfully authencticate the teacher
    access_token = create_access_token(data={"sub":str(teacher.id)})
    return {
        "access_token":access_token,
        "token_type":"bearer"
    }
    
# so this the sequence am using here 
# Find user
#    ↓
# Verify password
#    ↓
# Create JWT
#    ↓
# Return JWT
#####-------------- THE END OF AUTHENTICATING  A TEACHER -----######
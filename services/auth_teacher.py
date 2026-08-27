from sqlalchemy.orm import Session
from auth.security import hash_password
from  crud.teacher import (create_teacher,get_teacher_by_email,get_teacher_by_username)
from fastapi import HTTPException, status
from auth.security import(verify_password,create_access_token)





def Register_teacher():
    








   
# so this the sequence am using here 
# Find user
#    ↓
# Verify password
#    ↓
# Create JWT
#    ↓
# Return JWT
#####-------------- THE END OF AUTHENTICATING  A TEACHER -----######
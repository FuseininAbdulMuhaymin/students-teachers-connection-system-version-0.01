from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr

class TeacherModel(BaseModel):
    username:str
    email:EmailStr
    teacher_id:int
class TeacherCreate(TeacherModel):
   
    password:str
class Login(TeacherModel):
    email:str
    password:str 
class TokenResponse(BaseModel):
    access_token:str
    token_type:str
class TeacherUpdate(TeacherModel):
    password:str
class TeacherReponse(TeacherModel):
    password:str
class TeacherInDB(TeacherModel):
    hashed_password:str

    class Config:
        from_attribute = True
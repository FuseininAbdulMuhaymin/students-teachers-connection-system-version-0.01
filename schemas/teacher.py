from pydantic import BaseModel
from datetime import datetime
from pydantic import EmailStr

class TeacherModel(BaseModel):
    username:str
    email:EmailStr
class TeacherCreate(TeacherModel):
    email:EmailStr
    password:str
class TokenResponse(BaseModel):
    access_token:str
    token_type:str
class TeacherUpdate(TeacherModel):
    password:str
class TeacherReponse(TeacherModel):
    id:int
class TeacherInDB(TeacherModel):
    hashed_password:str

    class Config:
        from_attribute = True
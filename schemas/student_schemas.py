from pydantic import BaseModel


class StudentCreate(BaseModel):
    username: str
    email:str
    password:str 
    class_id: str

class TokenResponse(BaseModel):
    access_token:str
    token_type:str
class StudentResponse(BaseModel):
    id: int
    name: str
    class_id: int

    model_config = {
        "from_attributes": True
    }

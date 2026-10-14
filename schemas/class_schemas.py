from pydantic import BaseModel


class ClassCreate(BaseModel):
    name: str
    class_code:int

class ClassResponse(BaseModel):
    class_code: int
    name: str


    model_config = {
        "from_attributes": True
    }
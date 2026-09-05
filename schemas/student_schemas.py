from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    class_id: int


class StudentResponse(BaseModel):
    id: int
    name: str
    class_id: int

    model_config = {
        "from_attributes": True
    }
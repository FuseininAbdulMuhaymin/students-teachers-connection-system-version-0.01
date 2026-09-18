from pydantic import BaseModel


class ClassCreate(BaseModel):
    name: str
    teacher_id: str


class ClassResponse(BaseModel):
    id: int
    name: str
    teacher_id: int

    model_config = {
        "from_attributes": True
    }
from  pydantic import BaseModel
from datetime import datetime

class AssignmentModel(BaseModel):
    id:int
    created_at:datetime
    due_date:datetime
    
    
class  AssignmentCreate(BaseModel):
    title:str
    description:str
    due_date:datetime
    file_url:str
class AssignmentResponse(AssignmentModel):
    title:str

# class AssignmentResponse(BaseModel):
#     id: int
#     title: str
#     description: str
#     class_id: int
#     teacher_id: int
#     due_date: datetime
#     original_filename: str
#     file_url: str
#     created_at: datetime
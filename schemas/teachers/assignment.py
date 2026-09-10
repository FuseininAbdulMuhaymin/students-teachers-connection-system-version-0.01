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

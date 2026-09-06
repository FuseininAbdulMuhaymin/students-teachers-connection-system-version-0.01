from  sqlalchemy.orm import Session
from models.assignment import Assignment
from database import get_db



#Creating an assignment
def create_assignment(db:Session,title:str,description: str,file_url:str,date_due:str,teacher_id:str,class_id:str):
    assign = Assignment(
        title = title,
        description = description,
        file_url = file_url,
        date_due = date_due,
        class_id = class_id,
        teacher_id = teacher_id
    )
    
    db.add(assign)
    db.commit()
    db.refresh(assign)
    
    return assign

#Get an Assignment
def get_assignment(db:Session,assignment_id:int):
    return  
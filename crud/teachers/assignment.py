from  sqlalchemy.orm import Session
from models.assignment import Assignment
from datetime import datetime



#Creating an assignment
def create_assignment(db:Session,title:str,description: str,file_url:str,due_date:datetime,teacher_id:int,class_id:int):
    assign = Assignment(
        title = title,
        description = description,
        file_url = file_url,
        due_date = due_date,
        class_id = class_id,
        teacher_id = teacher_id
    )
    
    db.add(assign)
    db.commit()
    db.refresh(assign)
    
    return assign

#Get an Assignment
def get_assignment(db:Session,assignment_id:int):
    return(db.query(Assignment).filter(Assignment.id == assignment_id).first())

#deleting Assignment 
def delete_assignment(db:Session,assignment_id:int):
    assignment=(
        db.query(Assignment).filter(Assignment.id == assignment_id).first()
    )
     
    if not assignment:
        return None
    
    db.delete(assignment)
    db.commit()
    
    return assignment
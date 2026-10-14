from fastapi import HTTPException,status
from sqlalchemy.orm import Session
from crud.class_crud import classs_crud
from  schemas.class_schemas import ClassCreate
# from  crud.class_crud import create_new_class



def register_new_class(db:Session,class_in:ClassCreate):
    if classs_crud.get_new_class(db,class_code = class_in.class_code):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "this class id already exists"
        )
        
    return  classs_crud.create_new_class(
        db = db,
        name = class_in.name,
        class_code = class_in.class_code
    
    )
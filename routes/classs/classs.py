from sys import prefix
from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from database import get_db
from schemas.class_schemas import ClassCreate,ClassResponse
from  services.classs.auth_class import register_new_class


router = APIRouter(prefix="/class",tags=["Class"])


@router.post("/",response_model=ClassResponse)
async def create_new_class(class_in:ClassCreate,db:Session = Depends(get_db)):
    return register_new_class(db=db,class_in = class_in)
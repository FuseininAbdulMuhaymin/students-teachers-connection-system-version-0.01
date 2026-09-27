
from sqlalchemy import Column,ForeignKey,Integer,Table
from database import Base 


teacher_class_association = Table(
    "teacher_class",
    Base.metadata,
    
    
    Column("class_id",Integer,ForeignKey("classes.id",ondelete="CASCADE"),primary_key=True),
    Column("teacher_id",Integer,ForeignKey("teachers.id",ondelete="CASCADE"),primary_key=True)
)
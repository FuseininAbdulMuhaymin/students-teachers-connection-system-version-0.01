from sqlalchemy import Table,Column,Integer,ForeignKey
from database import Base

teacher_classes = Table("teacher_classes",Base.metedata,
    Column("teacher_id",Integer,ForeignKey("teacher.id"),primary_key=True),
                        
    Column("class_id",Integer,ForeignKey("class.id"),primary_key=True)         
    )
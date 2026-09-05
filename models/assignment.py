from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.orm import relationship


class  Assignment(Base):
    __tablename__ = "Assignments"
    
    id = Column(Integer,primary_key=True)
    title = Column(String,unique=True,nullable=False)
    description = Column(String)

    due_date =  Column(datetime,nullable=False)
    file_url = Column(String,nullable=False)
    created_at = Column(datetime, default=datetime.utcnow)
    
    teacher_id = Column(Integer,ForeignKey("teachers.id"))
    class_id =  Column(Integer,ForeignKey("classes.id"))
    
 
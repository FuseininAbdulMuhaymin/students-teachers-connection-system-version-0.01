from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from models.teacher_class import teacher_classes


class Teachers(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True,index=True,nullable=False)    
    hashed_password = Column(String,nullable=False)
  
# classes = relationship("Class", back_populates="teacher")
classes = relationship("Class",secondary="teacher_classes",back_populates="teachers ")
from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship



class Teachers(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True,index=True,nullable=False)    
    hashed_password = Column(String,nullable=False)
  
clussess = relationship("Class",secondary="teacher_classes",back_populates="teachers")
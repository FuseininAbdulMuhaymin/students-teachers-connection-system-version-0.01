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
  
    # FIX: Changed "student" to "students" to match back_populates
    students = relationship("Student", back_populates="teacher")
    
class Student(Base):
    __tablename__ ="students"
    
    id =  Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True)
    email = Column(String,unique=True) 
    
    teacher_id = Column(Integer,ForeignKey("teachers.id"))
    
    # Matches the updated attribute name in Teachers
    teacher = relationship("Teachers", back_populates="students")
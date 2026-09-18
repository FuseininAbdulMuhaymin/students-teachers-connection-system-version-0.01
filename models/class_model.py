from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from models.teacher_class import teacher_classes



class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    teacher_id = Column(Integer, ForeignKey("teachers.id"))

    # teacher = relationship("Teachers", back_populates="classes")
    # students = relationship("Class", back_populates="class_")
    
    teachers = relationship("Teachers",secondary="teacher_classes",back_populates="classes")
    
    students = relationship("Student", back_populates="class_")
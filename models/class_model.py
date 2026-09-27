from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.link import teacher_class_association


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    
    students  = relationship("Student", back_populates="class_")
    teachers  = relationship("Teachers",secondary=teacher_class_association,back_populates="classes")
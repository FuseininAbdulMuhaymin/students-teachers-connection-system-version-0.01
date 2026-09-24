from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from models.link import teacher_classes


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    teachers = relationship("Teachers",secondary=teacher_classes,back_populates="clusess")
    students = relationship("Teacher",back_populates="class_")
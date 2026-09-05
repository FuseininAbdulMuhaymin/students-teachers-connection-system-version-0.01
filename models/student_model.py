from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    class_id = Column(Integer, ForeignKey("classes.id"))

teacher = relationship("Teachers", back_populates="classes")
students = relationship("Student", back_populates="class_")
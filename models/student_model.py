from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    class_id = Column(String)


    class_id = Column(Integer, ForeignKey("classes.id"))

    class_= relationship("Class",back_populates="students")
from sqlalchemy import Column,Integer,String,ForeignKey
from database import Base
from sqlalchemy import DateTime
from sqlalchemy.orm import relationship
from models.link import teacher_class_association

class Teachers(Base):
    __tablename__ = "teachers"
    
    id = Column(Integer,primary_key=True)
    username = Column(String,unique=True)
    email = Column(String,unique=True,index=True,nullable=False)    
    hashed_password = Column(String,nullable=False)
    teacher_id = Column(String)
    # students = relationship("Student",secondary=teacher_class_association,back_populates="class_")
    classes = relationship("Class",secondary=teacher_class_association,back_populates="teachers")
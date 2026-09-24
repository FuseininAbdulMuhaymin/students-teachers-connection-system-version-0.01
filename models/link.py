from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base


teacher_classes = Table(
    "teacher_classes",
    Base.metadata,

    Column(
        "teacher_id",
        Integer,
        ForeignKey("teachers.id"),
        primary_key=True
    ),
#
    Column(
        "class_id",
        Integer,
        ForeignKey("classes.id"),
        primary_key=True
    )
)
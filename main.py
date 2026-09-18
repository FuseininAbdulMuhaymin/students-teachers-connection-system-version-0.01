from fastapi import FastAPI
from database import engine,Base
from routes.teachers.teacher import router as teacher_routers
from routes.teachers.assignment import router as teacher_assignment
from fastapi.staticfiles import StaticFiles
from routes.students.student import router as student_routers


#Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

#Register routers
app.include_router(teacher_routers)
app.include_router(teacher_assignment)
app.include_router(student_routers)
app.mount("/Files",StaticFiles(directory="uploads"),name = "files")
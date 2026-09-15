from fastapi import FastAPI
from database import engine,Base
from routes.teachers.teacher import router as teacher_routers
from routes.teachers.assignment import router as teacher_assignment
from fastapi.staticfiles import StaticFiles


#Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

#Register routers
app.include_router(teacher_routers)
app.include_router(teacher_assignment)
app.mount("/Files",StaticFiles(directory="uploads"),name = "files")
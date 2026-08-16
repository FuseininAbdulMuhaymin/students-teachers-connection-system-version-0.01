from fastapi import FastAPI
from database import engine,Base
from routes.teacher import router as teacher_routers

#Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

#Register routers
app.include_router(teacher_routers)
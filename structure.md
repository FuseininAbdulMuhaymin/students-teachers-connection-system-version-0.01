app/
│
├── models/
│   ├── teacher.py
│   ├── student.py
│   ├── class_model.py
│   ├── assignment.py
│   └── resource.py
│
├── schemas/
│   ├── teacher/
│   │   ├── auth.py
│   │   ├── assignment.py
│   │   └── resource.py
│   │
│   ├── student/
│   │   ├── auth.py
│   │   ├── assignment.py
│   │   └── resource.py
│   │
│   └── class_schema.py
│
├── routes/
│   ├── teacher/
│   │   ├── auth.py
│   │   ├── assignment.py
│   │   └── resource.py
│   │
│   ├── student/
│   │   ├── auth.py
│   │   ├── assignment.py
│   │   └── resource.py
│   │
│   └── class_routes.py
│
├── crud/
│   ├── teacher.py
│   ├── student.py
│   ├── assignment.py
│   └── resource.py
│
└── services/
    ├── teacher/
    │   ├── auth.py
    │   ├── assignment.py
    │   └── resource.py
    │
    └── student/
        ├── auth.py
        └── assignment.py




        STRUCTURE FOR  CREATING AN ASSIGNMENT 

        Teacher
   ↓
POST /assignments/
   ↓
Route receives:
   title
   description
   due_date
   file
   ↓
Service:
   validate teacher
   validate class
   save uploaded file
   generate file_url
   ↓
CRUD:
   create Assignment(...)
   ↓
PostgreSQL
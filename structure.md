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
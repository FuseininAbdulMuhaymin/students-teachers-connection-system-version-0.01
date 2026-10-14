                    TEACHER
                       │
                       │ creates
                       ↓
                 ASSIGNMENT
               ┌──────────────┐
               │ id            │
               │ teacher_id    │
               │ class_id      │
               │ title         │
               │ description   │
               │ due_date      │
               │ file_url      │
               └──────────────┘
                       │
                       │ assigned to
                       ↓
                    CLASS
                       │
             ┌─────────┼─────────┐
             ↓         ↓         ↓
          Student    Student   Student
             │         │         │
             └─────────┼─────────┘
                       │
                       │ submit
                       ↓
                  SUBMISSION
               ┌──────────────┐
               │ id            │
               │ student_id    │
               │ assignment_id │
               │ file_url      │
               │ submitted_at  │
               └──────────────┘
                       │
                       ↓
                  TEACHER
              views/downloads
              submissions


     so this is how the model to of subsmission look like 
     Submission
-------------------------
id
student_id
assignment_id
file_url
original_filename
submitted_at  

 students
    │
    │ student_id
    ↓
submissions
    │
    │ assignment_id
    ↓
assignments
    │
    │ teacher_id
    ↓
teachers




 THIS IS HOW  FLOW  FOR  TEACHERS RECIEVE THE SASSIGNMENT LOOK LIKE  Student uploads file
        ↓
FastAPI stores file
        ↓
PostgreSQL stores submission information
        ↓
Teacher requests submissions
        ↓
FastAPI returns submissions
        ↓
Teacher downloads student's file
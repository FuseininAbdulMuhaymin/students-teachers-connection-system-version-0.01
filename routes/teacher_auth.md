###### THIS  EXPLAINS  HOW 

THE FLOW  ROUTES OF TEACHER
Receive HTTP request
↓
Validate request data
↓
Call the appropriate logic
↓
Return HTTP response

     ####### THE REASON WHY WE USED db: Session = Depends(get_db) in the function of   registering a teacher 

1. the database is like a very big building and to work with it you need to connect to it and work
example
Route
  ↓
db
  ↓
Database
AUTHENTICATE A USER :Prove that the person making the request is the user they claim to be.


THIS IS AN EXAMPLE OF WHAT  THE FLOW  FOR  LOGGING IN A USER  AFTER  CREATING A USER AND REGISTERING USER
 User
 ↓
Provides username + password
 ↓
Backend finds the user
 ↓
Backend verifies password
 ↓
Password correct?
 ↓
YES
 ↓
Create JWT access token
 ↓
Give token to user

THIS IS WHAT  WE WILL DO 

Your backend will:

1.Find the teacher.
2.Verify the password.
3.Create an access token.
4.Return the token.


1.FINDING A USER 
when someone logs in 
username
   ↓
Database
   ↓
Teacher record

To do this  I need this crud function  get_teacher_by_username()

2.VERIFYING A  PASSWORD

I already have this function verify_password()  which compares  password user type and the hashed password stored  if the match   then it make succesfull   if not it make  failed

3.CREATE AN ACCES TOKEN
 
with create_access_token() 

After successfull  authenctication 

User authenticated
       ↓
create_access_token()
       ↓
JWT

jwt become the user's proof of authentication for subsequent  requests

4.THE REASON WHY WE NEED JWT
     the flow  of jwt 
Request
   ↓
JWT
   ↓
Verify JWT
   ↓
Who is this?
   ↓
teacher1   

           THIS A FULL FLOW OF AUTHENCTICATON TO BUILD
                           POST /auth/login
                       │
                       ▼
                    ROUTE
                       │
                       ▼
              authenticate_teacher()
                       │
                       ▼
             get_teacher_by_username()
                       │
                       ▼
                  PostgreSQL
                       │
                       ▼
                Teacher found?
                  /       \
                NO         YES
                │           │
                ▼           ▼
              401       verify_password()
                            │
                       ┌────┴────┐
                     Wrong     Correct
                       │          │
                       ▼          ▼
                      401    create_access_token()
                                  │
                                  ▼
                              JWT Token
                                  │
                                  ▼
                              Client
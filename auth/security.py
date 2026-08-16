from datetime import datetime, timedelta, timezone
from functools import lru_cache
import jwt
from pwdlib import PasswordHash
from pydantic_settings import BaseSettings, SettingsConfigDict
from crud.teacher import create_teacher

class Settings(BaseSettings):
    secret_key: str
    algorithm: str = "HS256"
    
    model_config = SettingsConfigDict(env_file=".env")
    
@lru_cache
def get_setting():
    return Settings()

#######--------- CREATING HASHING CONTEXT------#####
password_hashed= PasswordHash.recommended()

DUMMY_HASH = password_hashed.hash("dummypassword")

def hash_password(password: str) -> str:
    """Turns a plain password into a hashed one."""
    return password_hashed.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Compare the typed in password to the one in the database."""
    # FIXED: Changed from hash_password to hashed_password
    return password_hashed.verify(plain_password, hashed_password)

def authenticate_user(db, username: str, password: str):
    # Retrieve the user using your actual database helper
    user = db.get_user(username)  

    if not user:
        # Run dummy check even if user doesn't exist (timing attack prevention)
        verify_password(password, DUMMY_HASH)
        return False

    if not verify_password(password, user.hashed_password):
        return False

    return user

#### ---- JWT GENERATION UTILITY USING LOADED SETTING ------
# FIXED: Renamed to create_access_token and fixed timedelta keyword (minutes)
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    settings = get_setting()
    
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm
    )

    return encoded_jwt
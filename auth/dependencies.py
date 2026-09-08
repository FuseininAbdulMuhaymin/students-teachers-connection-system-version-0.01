from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt.exceptions import InvalidTokenError

from .security import get_setting
from database import get_db


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db=Depends(get_db)
):
    settings = get_setting()

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.secret_key,
            algorithms=[settings.algorithm]
        )

        teacher_id = payload.get("sub")

        if teacher_id is None:
            raise credentials_exception

    except InvalidTokenError:
        raise credentials_exception

    teacher = db.get_teacher_by_id(int(teacher_id))

    if teacher is None:
        raise credentials_exception

    return teacher
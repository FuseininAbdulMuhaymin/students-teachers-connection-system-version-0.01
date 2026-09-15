from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads/assignments")


async def save_assignment_file(file:UploadFile)->tuple[str,str]:
    if not file.filename:
        raise ValueError("File name is missing ")
        
    extension = Path(file.filename).suffix.lower()
    
    stored_filename = f"{uuid4()}{extension}"
    
    UPLOAD_DIR.mkdir(
        parents = True,
        exist_ok =True
    )
    
    file_path = UPLOAD_DIR/stored_filename
    
    
    with file_path.open("wb") as buffer:
        while chunk := await file.read(1024 * 1024):
            buffer.write(chunk)
            
    file_url = f"file/assignments/{stored_filename}"
    
    return  stored_filename
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
import crud

app = FastAPI()

@app.get("/users/{email}")
def read_user(email: str, db: Session = Depends(get_db)):
    try:
        user = crud.get_user_by_email(db, email)
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        print("ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
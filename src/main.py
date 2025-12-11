from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .models import User
from .dependencies import get_db

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user

@app.post("/users/adduser")
def add_user(username: str, password: str, db: Session = Depends(get_db)):
    user = User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "删除成功"}
    return {"message": "用户不存在"}

@app.put("/users/{user_id}")
def update_user(user_id: int, username: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = username
        user.password = password
        db.commit()
        return {"message": "更新成功"}
    return {"message": "用户不存在"}

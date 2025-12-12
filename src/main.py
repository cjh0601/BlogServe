from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .models import User
from .dependencies import get_db
from .httpmodels import UserCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

# 查询用户详情
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    return user


# 添加用户
@app.post("/users/adduser")
def add_user(user_data: UserCreate, db: Session = Depends(get_db)):
    user = User(username=user_data.username, password=user_data.password)
    print(user)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# 删除用户
@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "删除成功"}
    return {"message": "用户不存在"}

# 更新用户
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: UserCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.username = user_data.username
        user.password = user_data.password
        db.commit()
        db.refresh(user)
        return user
    return {"message": "用户不存在"}


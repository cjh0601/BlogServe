from .database import SessionLocal

# 每个请求自动创建一个 DB Session，并在结束后关闭
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 请求体模型
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
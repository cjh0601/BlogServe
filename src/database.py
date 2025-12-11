from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL=f"mysql+pymysql://root:{os.getenv('SQL_PASSWORD')}@{os.getenv('DATA_URL')}/{os.getenv('SQL_NAME')}?charset=utf8mb4"
engine = create_engine(
    DATABASE_URL,
    echo=True,              # 打印 SQL，调试用
    pool_pre_ping=True,     # 断线自动重连
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

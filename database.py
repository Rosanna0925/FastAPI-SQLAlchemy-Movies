# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")  # 如果沒設定就用 localhost
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

if os.getenv("DOCKER_ENV"):
    db_host=os.getenv("DB_HOST", "db")
else:
    db_host="localhost"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from fastapi import FastAPI
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

Base=declarative_base()



app=FastAPI()

@app.get("/")
async def read_root():
    return {"message":"Hello, World!"}
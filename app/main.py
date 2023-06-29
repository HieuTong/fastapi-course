from typing import Optional, List
from fastapi import FastAPI, HTTPException, Response, status, Depends
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from sqlalchemy.orm import Session
import models, schemas, utils
from database import engine, get_db
from routers import post, user, auth
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='080396', cursor_factory=RealDictCursor);
        cursor = conn.cursor()
        print("database connection successes")
        break
    except Exception as error:
        print("connect fail")
        print("error: ", error)
        time.sleep(2)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

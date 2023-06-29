from pydantic import BaseModel, EmailStr, Field;
from datetime import datetime;
from typing import Optional;

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating: Optional[int] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    # created_at: datetime 

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    email: EmailStr = Field(None, alias='my_email')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class UserLogin(BaseModel): 
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
from sqlalchemy import create_engine,Integer,String,Column,DateTime,Boolean
from sqlalchemy.orm import sessionmaker,DeclarativeBase

from os import getenv
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(getenv('DB_URL'),echo=True)

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer,primary_key=True)
    time = Column(DateTime)
    name = Column(String(100),nullable=False)
    text = Column(String)
    is_actual = Column(Boolean)


Base.metadata.create_all(engine)
SessionLocal = sessionmaker(engine)


    

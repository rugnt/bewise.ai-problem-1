import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Question(Base):
    __tablename__ = 'questions'

    pk = Column(Integer, primary_key=True)
    id = Column(Integer, unique=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow, index=True)


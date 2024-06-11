from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from database import Base


class Job(Base):
    __tablename__ = "job"

    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    create_date = Column(DateTime, default=func.now())

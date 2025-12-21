from sqlalchemy import Column, String, Integer, DateTime, JSON
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    status = Column(String, default="pending") # pending, processing, completed
    style = Column(String)
    output_urls = Column(JSON) # This stores the final AI links
    created_at = Column(DateTime, default=datetime.utcnow)

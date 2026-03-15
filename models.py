from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class Document(Base):

    __tablename__ = "documents_metadata"

    document_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    company_name = Column(String(255))
    document_type = Column(String(100))
    uploaded_by = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)
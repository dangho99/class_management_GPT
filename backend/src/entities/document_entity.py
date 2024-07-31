from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from src.entities.base import FivBaseAbstract
import os
from datetime import datetime


class Class_Entity(FivBaseAbstract):
    __tablename__ = "Document"
    document_id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey('Class.class_id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Teacher.teacher_id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    file_path = Column(String(255), nullable=False)
    upload_date = Column(DateTime, nullable=False)
    file_type = Column(String(20), nullable=False)
    size = Column(Integer, nullable=False)
    access_level = Column(String(20), nullable=False, default='public')
    subject = Column(String(100), nullable=False)
    status = Column(String(255), nullable=True)
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

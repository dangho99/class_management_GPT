from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from src.entities.base import FivBaseAbstract
import os
from datetime import datetime


class Assignment_Entity(FivBaseAbstract):
    __tablename__ = "Assignment"
    assignment_id = Column(Integer, primary_key=True, autoincrement=True)
    class_id = Column(Integer, ForeignKey('Class.class_id'), nullable=False)
    teacher_id = Column(Integer, ForeignKey('Teacher.teacher_id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    due_date = Column(DateTime, nullable=False)
    assigned_date = Column(DateTime, nullable=False)
    status = Column(String(20), nullable=False, default='pending')
    grade = Column(String(5), nullable=True)
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

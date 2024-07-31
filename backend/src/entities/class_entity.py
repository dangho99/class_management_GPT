from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.entities.base import FivBaseAbstract
import os
from datetime import datetime


class Class_Entity(FivBaseAbstract):
    __tablename__ = "Class"
    class_id = Column(Integer(), name='class_id', primary_key=True, autoincrement=True)
    class_name = Column(String(255), name='class_name')
    num_students = Column(Integer(), name='num_students')
    teacher_id = Column(String(255), name='teacher_id')
    room_number = Column(Integer(), name='room_number')
    schedule = Column(String(255), name='schedule')
    level = Column(String(255), name='level')
    description = Column(String(1024), name='description')
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

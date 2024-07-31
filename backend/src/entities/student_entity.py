from sqlalchemy import Column, Integer, String, DateTime, Boolean
from src.entities.base import FivBaseAbstract
import os
from datetime import datetime


class Student_Entity(FivBaseAbstract):
    __tablename__ = "Student"
    student_id = Column(Integer(), name='student_id', primary_key=True, autoincrement=True)
    first_name = Column(String(255), name='first_name')
    last_name = Column(String(255), name='last_name')
    class_name = Column(String(255), name='class_name')
    dob = Column(DateTime(), name='dob')
    login = Column(String(255), name='login')
    password = Column(String(255), name='password')
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

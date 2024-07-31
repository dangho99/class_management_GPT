from src.entities.base import FivBaseAbstract
from sqlalchemy import Column, Integer, String, DateTime, Float


class Teacher(FivBaseAbstract):
    __tablename__ = 'Teacher'
    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=True)
    hire_date = Column(DateTime, nullable=False)
    department = Column(String(50), nullable=False)
    qualification = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    address = Column(String(255), nullable=True)
    employment_status = Column(String(20), nullable=False)
    profile_picture = Column(String(255), nullable=True)  # Optional
    
    
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
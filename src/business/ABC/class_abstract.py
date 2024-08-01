from abc import ABCMeta, abstractmethod
from src.business.ABC.abstract import AbstractService

class ClassAbstract(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        super().__init__(trans_session)
        
    @abstractmethod
    def create(self, 
               class_name,
               num_students,
               teacher_id,
               room_number,
               schedule,
               level,
               description,
               **kwargs): raise NotImplementedError
    
    @abstractmethod
    def delete(self, class_id): raise NotImplementedError
    
    @abstractmethod
    def find(self, class_id): raise NotImplementedError
    
    @abstractmethod
    def update(self, class_id): raise NotImplementedError
    
    

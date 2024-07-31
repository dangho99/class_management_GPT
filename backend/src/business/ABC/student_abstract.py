from abc import ABCMeta, abstractmethod
from src.business.ABC.abstract import AbstractService

class StudentAbstract(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        super().__init__(trans_session)
        
    @abstractmethod
    def create(self,
               login,
               email,
               first_name,
               last_name,
               admin,
               language,
               status,
               password,
               **kwargs): raise NotImplementedError
        
    @abstractmethod
    def find(self, student): raise NotImplementedError
    
    @abstractmethod
    def delete(self, student): raise NotImplementedError
    
    @abstractmethod
    def update(self, student): raise NotImplementedError
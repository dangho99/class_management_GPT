from abc import ABCMeta, abstractmethod
from src.business.ABC.abstract import AbstractService

class DocumentAbstract(AbstractService):
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        super().__init__(trans_session)
        
    @abstractmethod
    def create(self,
               class_id,
               teacher_id,
               title,
               description,
               file_path,
               upload_date,
               size,
               access_level,
               subject,
               status,
               **kwargs): raise NotImplementedError
    
    @abstractmethod
    def read(self, document_id): raise NotImplementedError
    
    @abstractmethod
    def upload(self, document_id): raise NotImplementedError
    
    @abstractmethod
    def delete(self, document_id): raise NotImplementedError
    
    @abstractmethod
    def find(self, document_id): raise NotImplementedError
    
    
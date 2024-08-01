from src.business.ABC.student_abstract import StudentAbstract
from src.business.services.command.student.create import Create
from src.business.services.command.student.delete import Delete

class StudentService(StudentAbstract):
    def __init__(self, trans_session):
        super().__init__(trans_session)
        
    def create(self,
               login,
               email,
               first_name,
               last_name,
               admin,
               language,
               status,
               password,
               **kwargs):
        return Create(self.trans_session,login,email,first_name,last_name,admin,language,status,password).execute()
            
        pass
    
    # NOTE: unfunc
    def find(self, student):
        pass
    
    # NOTE: unfunc
    def delete_from_class(self, student_name):
        return Delete(self.trans_session, student_name).execute()
        
        pass
    
    # NOTE: unfunc
    def update(self, user_id):
        pass
    
    
    
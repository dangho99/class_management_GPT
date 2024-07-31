from src.business.services.student_service import StudentService
from src.ABC.ObjectAbstract import ObjectAbstract
from src import admin_session


class Dashboard(ObjectAbstract):
    def __init__(self, session_type) -> None:
        if session_type == "admin":
            self.trans_session = admin_session
        # if session_type == "teacher":
        #     self.trans_session = teacher_admin
        
        
    def get_student_service(self):
        return StudentService(self.trans_session)
        
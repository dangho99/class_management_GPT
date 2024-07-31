from src.business.services.command.student.__default__ import StudentCommand
from pyopenproject.business.util.filter import Filter
class Delete(StudentCommand):
    def __init__(self, trans_session, student_name):
        super().__init__(trans_session)
        self.student_name = student_name
        
    # def execute(self):
    #     try:
    #         service = self.trans_session.get_user_service()
    #         users = service.find_all([
    #                                      Filter("name", "=", [self.student_name])
    #                                  ],
    #                                  '[["id", "asc"]]')
    #         for usr in users:
    #             self.logger.info(usr)
    #             service.unlock(usr)
    #             service.delete(usr)
    #     except Exception as e:
    #         self.logger.warning(f"Cannot delete sudent due to {e}")
    #         print("Exit")
    #         raise SystemExit()
        
    
    def execute(self):
            service = self.trans_session.get_user_service()
            users = service.find_all([
                                         Filter("name", "=", [self.student_name])
                                     ],
                                     '[["id", "asc"]]')
            for usr in users:
                self.logger.info(usr)
                service.delete(usr)

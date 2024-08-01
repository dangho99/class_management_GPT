from src.business.services.command.student.__default__ import StudentCommand

class Create(StudentCommand):
    def __init__(self, trans_session, login, email, first_name, last_name, admin, language, status, password, **kwargs):
        super().__init__(trans_session)
        self.user = {
            "login": login,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "admin": admin,
            "language": language,
            "status": status,
            "password": password
        }
        
    def execute(self):
        try:
            service = self.trans_session.get_user_service()
            service.create(
                login=self.user['login'],
                email=self.user['email'],
                first_name=self.user['first_name'],
                last_name=self.user['last_name'],
                admin=self.user['admin'],
                language=self.user['language'],
                status=self.user['status'],
                password=self.user['password'],               
            )
        except Exception as e:
            self.logger.warning(f"Cannot create student due to {e}")
            raise SystemExit() 
            
    
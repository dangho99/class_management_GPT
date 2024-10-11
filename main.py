# import warnings
# warnings.filterwarnings("ignore")
# import os
# os.environ['envir'] = 'dev'
# os.environ["project_type"] = "openproject"
# os.environ["session"] = "admin"

# from src.services.heart_beat.GPUStatusService import GPUStatusService
# print(GPUStatusService().health_check())

# from src import admin_session, sql_session
# from src.services.project_type.openproject.admin import Admin
# admin_instance = Admin(session=os.environ["session"])

# # Call the _create method
# result = admin_instance._create()
# a = result.get_user_service

import warnings
warnings.filterwarnings("ignore")
import os
os.environ['envir'] = 'dev'
os.environ["project_type"] = "openproject"
os.environ["session"] = "admin"

from src import admin_session

from src.business import Dashboard

a = Dashboard(session_type='admin')
b = a.get_student_service()
b.create(
    login="dangho",
    email="dangho@openproject.com",
    first_name="Dang",
    last_name="Ho",
    admin=False,
    language="de",
    status="active",
    # Password minimum is 10 characters)
    password="Hohadang_123"
)
#b.delete_from_class("Hans3232 Wurst32323")
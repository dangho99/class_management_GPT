"""_summary_
"""
from src.utils.load_config import load_project_config
from functools import wraps
from src.ABC.ObjectAbstract import logger
import os
logger = logger.bind(class_name="src")
### Open Project configure
from pyopenproject.openproject import OpenProject
admin_session = False
try:
    op_cfg = load_project_config()
    op_client = OpenProject(
        url=op_cfg["url"],
        api_key=op_cfg["admin_api_key"],
    )
    admin_session = op_client
    logger.info("Admin Okay")
except Exception as e:
    logger.warning("Can't create teacher assignment session")

def admin_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        self = args[0]
        trans_session = kwargs.get('trans_session', self.session)  
        kwargs['trans_session'] = trans_session 
        if trans_session is not admin_session:
            return logger.warning("Not in admin session")
        logger.info("Begin running admin func: %s " % str(func))
        logger.info("Create session successfully")
        try:
            result = func(*args, **kwargs)
            logger.info("Admin session successfully")
            return result  
        except Exception as e:
            logger.error(f"Admin session was error because of {e}")
            raise SystemExit()
    return wrapper
    


    
### Database configure
from src.utils.load_config import load_sql_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
sql_session = False
sql_cfg = load_sql_config()
url = f"mysql+pymysql://{sql_cfg['user']}:{sql_cfg['password']}@{sql_cfg['host']}:{sql_cfg['port']}/{sql_cfg['database']}"
echo = os.environ.get("ECHO",False)
try:
    engine = create_engine(url=url)
    sql_session = sessionmaker(bind=engine)
    logger.info("SQL Okay")
except Exception as e:
    logger.warning("Can't create SQL session")


def sql_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global sql_session
        logger.info("Begin running transactional func:%s " % str(func))
        trans_session = sql_session()
        logger.info("Create session successfully")
        try:
            result = func(*args, trans_session=trans_session, **kwargs)
            trans_session.commit()
            logger.info("Commit session successfully")
            return result
        except Exception as e:
            logger.info("Begin rollback because e = %s" % str(e))
            trans_session.rollback()
            logger.info("Rollback successfully")
            raise e
        finally:
            trans_session.close()
    return wrapper



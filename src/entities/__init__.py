from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import database_exists, create_database
from src.ABC.ObjectAbstract import logger
from src import engine
import src.entities
import sys
import pkgutil
import inspect
import importlib


Base = declarative_base()
logger = logger.bind(class_name="entites")

def import_entities() -> list:
    package = src.entities
    entities = []
    for importer, modname, ispkg in pkgutil.iter_modules(package.__path__):
        module = importlib.import_module(f'{package.__name__}.{modname}')
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj):
                if str(module.__name__).split('.')[-1] == name:
                    logger.info('Getting entity = %s.%s' %
                                (module.__name__, name))
                    entities.append(obj)
        pass
    return entities

def db_upgrade():
    logger.info("Begin init DB fiv")
    try:
        if not database_exists(engine.url):
            create_database(engine.url)
            logger.info("Create database successfully")
        else:
            logger.info("Database database already exists.")
        import_entities()
        Base.metadata.create_all(engine)
        logger.info("Upgrade database sucessfully")
    except Exception as e:
        logger.error("Create DB failed with error: %s" % str(e))
        sys.exit(3)
    pass
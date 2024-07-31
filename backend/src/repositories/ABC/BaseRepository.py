from abc import ABC, abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract
from src.entities import Base
from sqlalchemy.orm.session import Session
from datetime import datetime
from sqlalchemy.engine.row import Row
from sqlalchemy import text
from sqlalchemy.engine.cursor import CursorResult
from sqlalchemy import func

class BaseRepository(ObjectAbstract):

    def __init__(self, session: Session, Entity, auto_commit=False):
        self.__session = session
        self.__Entity = Entity
        self.__auto_commit = auto_commit
        super().__init__()
        pass

    @property
    def session(self):
        return self.__session

    @property
    def entity(self):
        return self.__Entity

    @property
    def auto_commit(self):
        return self.__auto_commit
    
    # NOTE: new func
    def get_highest_batch_id(self, obj):
        self.logger.info('Begin retrieving highest id.')
        if not hasattr(obj, 'Batch_ID'):
            self.logger.error("The entity doesn't have an 'id' attribute")
            raise ValueError("The entity doesn't have an 'id' attribute")
        
        highest_id = self.__session.query(func.max(obj.Batch_ID)).scalar()
        
        self.logger.info(f'Successfully retrieved highest id: {highest_id}')
        return highest_id
    

    def get_by_key(self, key: str, value, trans_session=None):
        self.logger.info(f'Begin retrieving {key=}.')
        if not hasattr(self.__Entity, key):
            self.logger.error("The ojbect hasn't attribute '%s'" % key)
            raise ValueError("The ojbect hasn't attribute '%s'" % key)
        if trans_session:
            obj = trans_session.query(self.__Entity).filter_by(
                **{key: value}).first()
        else:
            obj = self.__session.query(
                self.__Entity).filter_by(**{key: value}).first()
        self.logger.info(f'Successfully retrieved {key=}.')
        return obj
    
    def get_obj_by_key(self, obj, search_key: str, search_value, return_key: str, trans_session=None):
        self.logger.info(f'Begin retrieving {return_key} based on {search_key}={search_value}.')
        
        if not hasattr(obj, search_key):
            self.logger.error(f"The object doesn't have attribute '{search_key}'")
            raise ValueError(f"The object doesn't have attribute '{search_key}'")
        
        if not hasattr(obj, return_key):
            self.logger.error(f"The object doesn't have attribute '{return_key}'")
            raise ValueError(f"The object doesn't have attribute '{return_key}'")
        
        session = trans_session or self.__session
        
        obj = session.query(obj).filter_by(**{search_key: search_value}).first()
        
        if obj is None:
            self.logger.warning(f"No object found with {search_key}={search_value}")
            return None
        
        return_value = getattr(obj, return_key)
        
        self.logger.info(f'Successfully retrieved {return_key}={return_value} based on {search_key}={search_value}.')
        return return_value
    
    def get_by_key_all(self, key: str, value, trans_session=None):
        self.logger.info(f'Begin retrieving {key=}.')
        if not hasattr(self.__Entity, key):
            self.logger.error("The ojbect hasn't attribute '%s'" % key)
            raise ValueError("The ojbect hasn't attribute '%s'" % key)
        if trans_session:
            obj = trans_session.query(self.__Entity).filter_by(
                **{key: value}).all()
        else:
            obj = self.__session.query(
                self.__Entity).filter_by(**{key: value}).all()
        self.logger.info(f'Successfully retrieved {key=}.')
        return obj


    def get_first_item_by_keys(self, trans_session=None, **kwargs):
        self.logger.info(f'Begin retrieving %s.' % str(kwargs.keys()))
        for key in kwargs.keys():
            if not hasattr(self.__Entity, key):
                self.logger.error("The ojbect hasn't attribute '%s'" % key)
                raise ValueError("The ojbect hasn't attribute '%s'" % key)
        obj = None
        if trans_session:
            obj = trans_session.query(self.__Entity).filter_by(
                **kwargs).first()
        else:
            obj = self.__session.query(
                self.__Entity).filter_by(**kwargs).first()
        self.logger.info(f'Successfully retrieved %s.' % str(kwargs.keys()))
        return obj

    def get_all_item_by_keys(self, trans_session=None, **kwargs) -> list:
        self.logger.info(f'Begin retrieving %s.' % str(kwargs.keys()))
        for key in kwargs.keys():
            if not hasattr(self.__Entity, key):
                self.logger.error("The ojbect hasn't attribute '%s'" % key)
            raise ValueError("The ojbect hasn't attribute '%s'" % key)
        if trans_session:
            obj = trans_session.query(self.__Entity).filter_by(
                **kwargs).all()
        else:
            obj = self.__session.query(
                self.__Entity).filter_by(**kwargs).all()
        #self.logger.info(f'Successfully retrieved {key=}.')

    def parse(self, obj: Row):
        self.logger.debug("obj: %s" % str(obj))
        obj = obj._mapping
        tmp_dict = {column: obj.get(column)
                    for column in self.__Entity.__table__.columns.keys()}
        return self.__Entity(**tmp_dict)
        pass

    def parses(self, objs: CursorResult):
        self.logger.debug("len of objs: %s" % str(objs.rowcount))
        result = []
        for obj in objs:
            result.append(self.parse(obj=obj))
        return result

    def create(self, obj, trans_session=None):
        self.logger.info("Begin create new %s" % str(obj))
        if trans_session :
            trans_session.add(obj)
            return obj
        else:
            self.__session.add(obj)
            if self.auto_commit:
                try:
                    self.__session.commit()
                except Exception as e:
                    self.logger.error(
                        "Saving data to the database is error: %s" % str(e))
                    raise e
        return obj
        pass

    def get_by_id(self, id: int, trans_session=None):
        self.logger.info(f'Begin retrieving {id=}.')
        if not hasattr(self.__Entity, 'id'):
            self.logger.error("The ojbect hasn't attribute 'id'")
            raise ValueError("The ojbect hasn't attribute 'id'")
        if trans_session:
            obj = trans_session.query(self.__Entity).filter_by(id=id).first()
        else:
            obj = self.__session.query(self.__Entity).filter_by(id=id).first()
        self.logger.info(f'Successfully retrieved {id=}.')
        return obj
    
    def get_by_obj_id(self, obj, id: int, trans_session=None):
        self.logger.info(f'Begin retrieving {id=}.')
        if not hasattr(obj, 'Batch_ID'):
            self.logger.error("The ojbect hasn't attribute 'id'")
            raise ValueError("The ojbect hasn't attribute 'id'")
        if trans_session:
            res = trans_session.query(obj).filter_by(Batch_ID=id).first()
        else:
            res = self.__session.query(obj).filter_by(Batch_ID=id).first()
        self.logger.info(f'Successfully retrieved {id=}.')
        return res

    def update_by_id(self, id: int, trans_session=None, **kwargs):
        if not hasattr(self.__Entity, 'id'):
            self.logger.error("The %s hasn't attribute 'id'" %
                              self.__Entity.__class__.__name__)
            raise ValueError("The %s hasn't attribute 'id'" %
                             self.__Entity.__class__.__name__)
        obj = self.get_by_id(id=id, trans_session=trans_session)
        return self.update(obj=obj, **kwargs)
        pass

    def update_obj_by_id(self, obj , id: int, trans_session=None, **kwargs):
        if not hasattr(obj, 'Batch_ID'):
            self.logger.error("The %s hasn't attribute 'id'" %
                              obj.__class__.__name__)
            raise ValueError("The %s hasn't attribute 'id'" %
                             obj.__class__.__name__)
        obj = self.get_by_obj_id(obj=obj, id=id, trans_session=trans_session)
        return self.update(obj=obj, **kwargs)
        pass

    def update(self, obj, **kwargs):
        for key, value in kwargs.items():
            if hasattr(obj, key):
                setattr(obj, key, value)
            else:
                self.logger.warning("The ojbect hasn't attribute '%s'" % key)

        if hasattr(obj, 'last_modified_time'):
            setattr(obj, 'last_modified_time', datetime.now())
        if self.__auto_commit:
            try:
                self.__session.commit()
            except Exception as e:
                self.logger.error(
                    "Update data to the database is error: %s" % str(e))
                raise e
        return True
        pass

    def commit(self):
        try:
            self.__session.commit()
        except Exception as e:
            
            self.logger.error(
                "Commit transaction error %s" % str(e))
            self.__session.rollback()
            self.logger.info("Rollback transaction successfully.")
            return False
        return True

    def get_by_naitive_query(self, native_query: str, params: dict):
        self.logger.info("begin executing native_query")
        self.logger.debug("native_query: %s, params: %s" %
                          (native_query, params))
        try:
            native_query = text(native_query)
            rows = self.__session.execute(
                statement=native_query, params=params)
            result = self.parses(rows)
            return result
            pass
        except Exception as e:
            self.logger.error(f"{e=}")
            raise None
            pass
        pass

    def close(self):
        self.logger.info("Begin closing session %s" % self.__session)
        if self.__session is None:
            self.logger.warn("Session is None")
        else:
            self.__session.close()
            self.logger.info("Close session %s successfully" % self.__session)
        pass

    def delete(self, obj):
        pass

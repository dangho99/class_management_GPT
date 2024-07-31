
from src.entities import Base
from src.utils.log import get_logger
from src.ABC.ObjectAbstract import logger
import logging
import copy

class FivBaseAbstract(Base):
    __abstract__ = True

    def __init__(self, **kwargs) -> None:
        self.__logger = logger
        super().__init__(**kwargs)

    def to_dict(self, ignore_cols=[]) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns if column.name not in ignore_cols}

    def __str__(self) -> str:
        return str(self.to_dict())

    def __eq__(self, value: object) -> bool:
        if self.__class__ != value.__class__:
            return False
        return self.__str__() == value.__str__()

    def copy(self):
        return copy.deepcopy(self)

    @property
    def logger(self):
        return self.__logger
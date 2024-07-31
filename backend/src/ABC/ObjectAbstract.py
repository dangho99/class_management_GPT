
from abc import ABC, abstractmethod
import json
from src.utils.log import get_logger
import loguru
from loguru import logger
import sys
fmt = "<g>{time}</> | <lvl>{level}</> | <e> {extra[class_name]} </>|<c>{name}:{function}:{line}</> - {message}"
logger.remove() 
logger.add(sys.stderr, format=fmt)

class ObjectAbstract(ABC):
    
    def __init__(self) -> None:
        self.__logger = logger.bind(class_name=self.__class__.__name__)
        super().__init__()
    
    def to_dict(self) -> dict:
        result = {}
        for key, value in self.__dict__.items():
            result[key.split(self.__class__.__name__)[-1]] = value
        return result
    
    def __str__(self) -> str:
        return str(self.to_dict())

        
    def __eq__(self, value:object) -> bool:
        if self.__class__ != value.__class__:
            return False
        return self.__str__() ==  value.__str__()
    
    
    @property
    def logger(self) -> loguru.logger:
        return self.__logger
    
    






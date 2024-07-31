from abc import ABCMeta, abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract

class LLMCommand(ObjectAbstract):
    __metaclass__ = ABCMeta
    
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def execute(self): raise NotImplementedError

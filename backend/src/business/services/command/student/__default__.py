from abc import abstractmethod, ABCMeta
from src.business.services.command.command import Command


class StudentCommand(Command):
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        self.trans_session = trans_session
        super().__init__()

    @abstractmethod
    def execute(self): raise NotImplementedError

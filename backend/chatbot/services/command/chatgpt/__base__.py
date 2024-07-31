from chatbot.services.command.command import LLMCommand
from abc import abstractmethod, ABCMeta

class ChatGPTCommand(LLMCommand):
    __metaclass__ = ABCMeta

    def __init__(self, trans_session):
        self.trans_session = trans_session
        super().__init__()

    @abstractmethod
    def execute(self): raise NotImplementedError
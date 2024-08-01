from abc import ABCMeta
from src.chatbot.helper.validator import Case

class Prompting(ABCMeta):
    def __init__(self, **kwargs):
        pass
    
    def get_context(self):
        pass
    
    
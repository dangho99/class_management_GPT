from src.chatbot import Chatbot
from abc import ABC, abstractmethod

class AgentManagement(ABC):
    def __init__(self, agent_name, trans_session) -> None:
        self.agent_name = agent_name
        self.trans_session = trans_session
        super().__init__()
        
    @abstractmethod
    def execute(self, query):
        pass
    
    
    
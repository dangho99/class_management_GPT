from src.chatbot.agents import AgentManagement
import os

class ClassAgent(AgentManagement):
    def __init__(self, trans_session) -> None:
        super().__init__(trans_session)
        
    def execute(self, query):
        pass
    
agent = ClassAgent(trans_session=os.environ["envir"])    
    
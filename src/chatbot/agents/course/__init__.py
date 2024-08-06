from src.chatbot.agents import ChatBot
import os

class CourseAgent(ChatBot):
    def __init__(self, trans_session) -> None:
        super().__init__(trans_session)
        
    def execute(self, query):
        pass
    
agent = CourseAgent(trans_session=os.environ["session"])
from src.chatbot import ChatBot
from abc import abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract

class Command(ObjectAbstract):
    def __init__(self, chatbot_type) -> None:
        super().__init__()
        self.chatbot_type = chatbot_type
        self.bot = ChatBot(model_key=chatbot_type)
        self.agent = None
        
    def get_agent(self, name):
        self.agent = self.bot.get_agent(agent_name=name)
        return self.agent
    
    def run(self, query):
        if self.agent is None:
            self.logger.error("Hasn't assign any agent. Exit now")
            raise SystemExit()
        result = self.agent.execute(query)
        self.logger.info(result)
        
        return result
        
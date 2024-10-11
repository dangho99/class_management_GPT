from src.chatbot import ChatBot
from abc import abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract

class Command(ObjectAbstract):
    def __init__(self, chatbot_type) -> None:
        super().__init__()
        self.chatbot = ChatBot(model_key=chatbot_type)
        self.agent = None

    def get_agent(self, name):
        self.agent = self.chatbot.get_agent(agent_name=name)
        return self.agent

    def run(self, query):
        if self.agent is None:
            self.logger.error("Hasn't assigned any agent. Exit now")
            raise SystemExit()
        self.agent.update_stats(query)
        result = self.agent.execution_strategy.execute(query)
        self.logger.info(result)
        return result
        
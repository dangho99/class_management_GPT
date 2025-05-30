from abc import ABC, abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract
#from src.chatbot.bot import Loader
import importlib


class ChatBot(ObjectAbstract):
    def __init__(self, model_key) -> None:
        super().__init__()
        self.model_key = model_key
        self.model = None  # You might want to load the model here
        self.agent = None

    def get_agent(self, agent_name):
        if self.agent is None:
            self.load_agent(agent_name)
        return self.agent

    def load_agent(self, agent_name):
        try:
            module = importlib.import_module(f"src.chatbot.agents.{agent_name}")
            agent_class = getattr(module, "agent")
            self.agent = agent_class(self)
        except ImportError:
            self.logger.error(f"Invalid agent name: {agent_name}. Module not found.")
            raise SystemExit()
        except AttributeError:
            self.logger.error(f"Agent class not found in module: {agent_name}")
            raise SystemExit()

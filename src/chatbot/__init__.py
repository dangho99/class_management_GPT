from openai import OpenAI
from abc import abstractmethod
from src.ABC.ObjectAbstract import ObjectAbstract
from src.utils.load_config import load_chatbot_config
from src.chatbot.agents.base import AgentManagement
from src.chatbot.prompt import Prompting

llm_cfg = load_chatbot_config()
model = OpenAI(api_key=llm_cfg["api_key"])


class Chatbot(ObjectAbstract):
    def __init__(self) -> None:
        self.agents = []
        super().__init__()
        
    def add_agents(self, agent: AgentManagement):
        self.agents.append(agent)
        
    def process(self,query) -> Prompting:
        #return Prompting(get_enitities_matching(query))'
        pass
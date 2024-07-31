from src.chatbot.services.chatgpt import ChatGPTService
from src.chatbot.services.mistral import MistralService
from src.chatbot.services.llama import LlamaService
from src.ABC.ObjectAbstract import ObjectAbstract

class LLM(ObjectAbstract):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()
        
    def load(self):
        if self.name == 'chatgpt':
            return ChatGPTService()
        if self.name == 'mistral':
            return MistralService()
        if self.name == 'llama':
            return LlamaService
        
        
    def agent_health_check():
        pass
    
    
        
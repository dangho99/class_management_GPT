from abc import ABC, abstractmethod
from src.chatbot.bot.chatgpt.execution import ChatGPTExecutionStrategy
from src.chatbot.bot.gemini.execution import GeminiExecutionStrategy


class ExecutionStrategyFactory:  
    @staticmethod
    def get_strategy(model_key: str):
        strategies = {
            "chatgpt": ChatGPTExecutionStrategy(),
            "gemini": GeminiExecutionStrategy(),
        }
        return strategies.get(model_key.lower())
    
    
    


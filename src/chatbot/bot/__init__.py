from abc import abstractmethod, ABC
import loguru
from loguru import logger
import sys
from src.ABC.ObjectAbstract import ObjectAbstract
from src.chatbot.bot.execution import ExecutionStrategy
from src.chatbot.bot.chatgpt import ChatGPTExecutionStrategy
from src.chatbot.bot.gemini import GeminiExecutionStrategy
import importlib
fmt = "<g>{time}</> | <lvl>{level}</> | <e> {extra[class_name]} </>|<c>{name}:{function}:{line}</> - {message}"
logger.remove() 
logger.add(sys.stderr, format=fmt)


class Chatbot(ABC):
    def __init__(self, model_key) -> None:
        self.model_key = model_key
        self.model = None
        self.__logger = loguru.logger.bind(class_name=self.__class__.__name__)

    def get_model(self):
        if self.model is None:
            self.load_model()
        return self

    def load_model(self):
        try:
            module = importlib.import_module(f"src.chatbot.bot.{self.model_key}")
            self.model = getattr(module, "model")
        except ImportError:
            raise ValueError(f"Invalid model key: {self.model_key}. Module not found.")
        except AttributeError:
            raise ValueError(f"Model class not found in module: {self.model_key}")

    @property
    def logger(self) -> loguru.logger:
        return self.__logger
    


class ExecutionStrategyFactory:
    @staticmethod
    def get_strategy(model_key: str) -> ExecutionStrategy:
        strategies = {
            "chatgpt": ChatGPTExecutionStrategy(),
            "gemini": GeminiExecutionStrategy(),
        }
        return strategies.get(model_key.lower(), ChatGPTExecutionStrategy())
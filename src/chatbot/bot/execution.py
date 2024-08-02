from abc import ABC, abstractmethod

class ExecutionStrategy(ABC):
    @abstractmethod
    def execute(self, query: str):
        pass

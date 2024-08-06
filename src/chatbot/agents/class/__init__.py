from src.chatbot.agents import BaseAgent

class ClassAgent(BaseAgent):
    def __init__(self, agent_management) -> None:
        super().__init__(agent_management)

    def execute(self, query: str):
        self.update_stats(query)
        result = self.execution_strategy.execute(query)
        print(f"ClassAgent {result}")


def agent(agent_management):
    return ClassAgent(agent_management)
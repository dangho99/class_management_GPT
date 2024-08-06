from src.chatbot.bot.execution import ExecutionStrategyFactory

class BaseAgent:
    def __init__(self, agent_management) -> None:
        self.agent_management = agent_management
        self.model_key = agent_management.model_key
        self.model = agent_management.model
        self.tasks_completed = 0
        self.last_query = None
        self.execution_strategy = ExecutionStrategyFactory.get_strategy(self.model_key)

    @property
    def name(self) -> str:
        return self.__class__.__name__

    def get_status(self) -> str:
        return f"Status: Active | Last Query: {self.last_query or 'None'}"

    def reset_stats(self) -> None:
        self.tasks_completed = 0
        self.last_query = None

    def __str__(self):
        return (f"  Agent: {self.name}\n"
                f"  Model Key: {self.model_key}\n"
                f"  Model Type: {self.model.__class__.__name__ if self.model else 'Not loaded'}\n"
                f"  Tasks Completed: {self.tasks_completed}\n"
                f"  Last Query: {self.last_query or 'None'}\n"
                f"  Status: {self.get_status()}")

    def update_stats(self, query):
        self.last_query = query
        self.tasks_completed += 1
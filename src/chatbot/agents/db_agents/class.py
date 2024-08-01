from src.chatbot.agents.base import AgentManagement

class ClassAgent(AgentManagement):
    def __init__(self, agent_name, trans_session) -> None:
        super().__init__(agent_name, trans_session)
        
    def execute(self, query):
        pass
    
    
    
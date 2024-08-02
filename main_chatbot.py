import os
os.environ["envir"] = "dev"
os.environ["project_type"] = "openproject"
os.environ["session"] = "admin"
chatbot_type = os.environ["chatbot_type"] = "chatgpt"

from src.chatbot import AgentManagement

agent_management = AgentManagement(model_key=chatbot_type)

agent_management.get_model()

assignment_agent = agent_management.get_agent(agent_name='assignment')

query = assignment_agent.execute("start")
query = assignment_agent.execute("last")

print(assignment_agent)

import os
from loguru import logger
logger = logger.bind(class_name="root")
os.environ["envir"] = "dev"
os.environ["project_type"] = "openproject"
os.environ["session"] = "admin"
chatbot_type = os.environ["chatbot_type"] = "gemini"

from src.chatbot.tasks.command.run import Command

a = Command(chatbot_type=chatbot_type)
a.get_agent("assignment")

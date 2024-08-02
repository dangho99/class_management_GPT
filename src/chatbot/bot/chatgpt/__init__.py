from openai import OpenAI
from src.utils.load_config import load_chatbot_config
from src.chatbot.bot.execution import ExecutionStrategy

llm_cfg = load_chatbot_config()
model = OpenAI(api_key=llm_cfg["api_key"])

class ChatGPTExecutionStrategy(ExecutionStrategy):
    def execute(self, query: str):
        return f"ChatGPT executed: {query}"
import google.generativeai as genai
from src.chatbot.bot.gemini.gemini_config import safety_settings, generation_config
from src.utils.load_config import load_chatbot_config
import os
from src.chatbot.bot.execution import ExecutionStrategy

bot_cfg = load_chatbot_config()
genai.configure(api_key=bot_cfg["api_key"])
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

class GeminiExecutionStrategy(ExecutionStrategy):
    def execute(self, query: str):
        return f"Gemini executed: {query}"
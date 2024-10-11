import google.generativeai as genai
from src.chatbot.bot.gemini.gemini_config import safety_settings, generation_config
from src.utils.load_config import load_chatbot_config
import os

bot_cfg = load_chatbot_config()
genai.configure(api_key=bot_cfg["api_key"])
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

def get_gemini_response(query):
    try:
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
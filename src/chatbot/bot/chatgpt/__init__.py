from openai import OpenAI
from src.utils.load_config import load_chatbot_config

llm_cfg = load_chatbot_config()
model = OpenAI(api_key=llm_cfg["api_key"])


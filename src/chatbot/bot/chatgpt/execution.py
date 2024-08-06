from src.chatbot.bot.chatgpt import model

class ChatGPTExecutionStrategy:
    def execute(self, query: str):
        final_message = 2
        return f"ChatGPT executed: {final_message}"
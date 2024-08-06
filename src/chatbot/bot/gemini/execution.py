from src.chatbot.bot.gemini import get_gemini_response

class GeminiExecutionStrategy:
    def execute(self, query: str):
        answer = get_gemini_response(query)
        return f"Gemini executed: {answer}"
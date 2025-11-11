import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()


class GeminiLLM:
    def __init__(self):
        # Available models: gemini-2.5-flash, gemini-2.5-pro, gemini-2.0-flash
        # gemini-2.5-flash is recommended for free tier (faster and cheaper)
        # gemini-2.0-flash-exp is experimental and may have quota limits
        self.model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")  # Default to gemini-2.5-flash
        self.temperature = 0
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")
        
        self.llm = ChatGoogleGenerativeAI(
            model=self.model,
            temperature=self.temperature,
            google_api_key=self.api_key
        )

    def get_llm(self):
        return self.llm
    

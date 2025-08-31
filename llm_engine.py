from dotenv import load_dotenv
import os
from openai import OpenAI
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class LLMEngine:
    def __init__(self):
        # Initialize OpenAI client
        self.client = OpenAI(api_key=api_key)

    def generate_overview_by_chunk(self, prompt: str) -> str:
        """
        Generates an overview/summary from chunked data using GPT-3.5.
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",  # Cheaper model
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes search results."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Engine:
    def __init__(self, query):
        self.query = query

    def generate_response(self):
        # Simulate a response from the language model
        print(os.getenv('LANG_SEARCH'))
        response = requests.post(
            "https://api.langsearch.com/v1/web-search",
            headers={
                "Authorization": f"Bearer {os.getenv('LANG_SEARCH')}",
                "Content-Type": "application/json"
            },
            json={"query": self.query}
        )
        return response.json()

import openai
import os
from interfaces import AIServiceInterface


class OpenAIService(AIServiceInterface):
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        openai.api_key = self.openai_api_key

    def ask_ai(self, system_prompt, user_prompt, model="gpt-4o-mini", token_limit=50):
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=token_limit
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise ValueError(f"ask_ai failed: {user_prompt}") from e
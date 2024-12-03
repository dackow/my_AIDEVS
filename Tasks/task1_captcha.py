import os
from interfaces import TaskInterface, AIServiceInterface
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Define credentials
USERNAME = os.getenv('TASK1_USERNAME')
PASSWORD = os.getenv('TASK1_PASSWORD')
URL = os.getenv('TASK1_URL')

class Task1_captcha(TaskInterface):
    def __init__(self):
        self.username = USERNAME
        self.password = PASSWORD
        self.url = URL        

    def execute(self, ai_model: AIServiceInterface):
        session = requests.Session()
        response = session.get(URL)
        response.raise_for_status()  # Ensure the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        question_element = soup.find(id="human-question")
        if question_element is None:
            raise ValueError("Could not find the human question on the page.")
        question_text = question_element.get_text(strip=True)

        system_message = "You are a helpful assistant. Answet to the question with only one word"
        user_message = question_text

        answer = ai_model.ask_ai(system_message, user_message)

        payload = {
            "username": self.username,
            "password": self.password,
            "answer": answer
        }

        # Step 5: Post the form data back to the website
        post_response = session.post(URL, data=payload)
        post_response.raise_for_status()  # Ensure the request was successful

        # Step 6: Print the response to check if submission was successful
        print(post_response.text)

        return post_response.text













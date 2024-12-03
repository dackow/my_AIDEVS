from abc import ABC, abstractmethod

class TaskInterface(ABC):
    @abstractmethod
    def execute(self):
        pass

class AIServiceInterface(ABC):
    @abstractmethod
    def ask_ai(self, system_prompt, user_prompt, model="gpt-4o-mini", token_limit=50):
        pass


from interfaces import TaskInterface,AIServiceInterface
import re

class TaskRunner:
    def __init__(self):
        self.task_model_pairs = []

    def add_task(self, task:TaskInterface, model:AIServiceInterface):
        self.task_model_pairs.append((task, model))

    def find_flags(self, text:str):
        # Pattern to match "FLG:xxx" where xxx is any alphanumeric value
        pattern = r'FLG:([a-zA-Z0-9]+)'
        matches = re.findall(pattern, text)
        return matches

    def run_all_tasks(self):
        for task, model in self.task_model_pairs:
            result = task.execute(model)
            flag = self.find_flags(result)
            print(f"Task {task.__class__.__name__} executed. Flags: {flag}")


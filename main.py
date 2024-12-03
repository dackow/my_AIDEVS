from task_runner import TaskRunner
from Services.openai_service import OpenAIService

from Tasks.task1_captcha import Task1_captcha


def main():    
    openai = OpenAIService()

    task_runner = TaskRunner()

    task1 = Task1_captcha()
    task_runner.add_task(task1, openai)

    task_runner.run_all_tasks()

    pass


if __name__ == "__main__":
    main()

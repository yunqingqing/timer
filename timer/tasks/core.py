# task manager module
from timer.common.load_driver import load_driver
from timer.config import settings


class Manager():
    dirver_namespace = "timer.tasks"

    def __init__(self):
        self.driver = load_driver(self.dirver_namespace, settings.tasks['backend'])

    def create_task(self):
        pass

    def get_tasks(self):
        return self.driver.get_tasks()

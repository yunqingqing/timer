# schedule manager module
from timer.common.load_driver import load_driver
from timer.config import settings


class Manager():

    def __init__(self):
        self.driver = load_driver(settings.scheduler['provider'])

    def add_task(self, task):
        return self.driver.add_task(task)

    def cancle_task(self):
        return self.driver.cancle_task()

    def get_tasks(self):
        return self.driver.get_tasks()

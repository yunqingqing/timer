import json

from timer.tasks.backends import base
from timer.config import settings


class Task(base.TaskDriveBase):

    def create_task(self, task):
        pass

    def get_tasks(self):
        with open(settings.tasks['uri']) as f:
            json_data = json.load(f)
        return json_data

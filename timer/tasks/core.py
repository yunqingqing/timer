# task manager module
from timer.common.load_driver import load_driver
from timer.config import settings


class Task():
    _attrs = ["command", "delay", "priority", "is_period"]

    def __init__(self, task_json):
        self._task = task_json

    def __getattribute__(self, attr):
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            if attr not in self._attrs:
                raise
            # __getattr__ won't find properties
            return self._task.get(attr, "")

    def __repr__(self):
        return "<%s: %s>" % (self.__class__.__name__,
                             dict((attr, getattr(self, attr))
                                  for attr in self._attrs
                                  if hasattr(self, attr)))

    def to_dict(self):
        obj = {}
        for key in self._attrs:
            obj[key] = self._task.get(key, None)
        return obj


class Manager():

    def __init__(self):
        self.driver = load_driver(settings.tasks['backend'])

    def create_task(self):
        pass

    def get_tasks(self):
        return self.driver.get_tasks()

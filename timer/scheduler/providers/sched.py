import logging
import sched
import subprocess
import time

from timer.scheduler.providers import base


logger = logging.getLogger(__name__)


def run_task(sc, task):
    # do you stuff
    cmd_args = task.command.split(" ")
    logger.info("run {}...", " ".join(cmd_args))
    subprocess.run(cmd_args)
    if task.is_period:
        sc.enter(task.delay, task.priority, task.period_task, (sc, task,))


class Sched(base.SchedulerDriveBase):

    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def add_task(self, task):
        self.scheduler.enter(task.delay, task.priority, run_task, (self.scheduler, task))
        self.scheduler.run()

    def cancle_tasks(self):
        pass

    def get_tasks(self):
        return self.scheduler.queue

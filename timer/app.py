import logging
import threading

from timer.config import settings
from timer.tasks.core import Manager, Task
from timer.scheduler.core import Manager as SchedManager

from sanic import Sanic
from sanic.response import json

logger = logging.getLogger(__name__)
task_manager = Manager()
sched_manager = SchedManager()
tasks = task_manager.get_tasks()
app = Sanic(log_config=settings.LOGGING)


def _load_task():
    for k, v in tasks.items():
        task = Task(v)
        logger.info("add task, {}".format(task))
        sched_manager.add_task(task)


def load_task():
    scheduler_task = threading.Thread(target=load_task)
    scheduler_task.start()


@app.route("/sched_task")
async def test(request):
    tq = sched_manager.get_tasks()
    return json({"sched_tasks": [event.argument[1].to_dict() for event in tq]})


def start_server():
    app.run(host="0.0.0.0", port=8081, backlog=128)


def run():
    load_task()
    start_server()


if __name__ == "__main__":
    run()

import threading
from logging.config import dictConfig

from timer.tasks.core import Manager, Task
from timer.scheduler.core import Manager as SchedManager

from flask import Flask
from flask import jsonify

task_manager = Manager()
sched_manager = SchedManager()
tasks = task_manager.get_tasks()
app = Flask(__name__)


def _load_task():
    for k, v in tasks.items():
        task = Task(v)
        app.logger.info("add task, {}".format(task))
        sched_manager.add_task(task)


def load_task():
    scheduler_task = threading.Thread(target=_load_task)
    scheduler_task.start()


@app.route("/sched_task")
def test():
    tq = sched_manager.get_tasks()
    return jsonify({"sched_tasks": [event.argument[1].to_dict() for event in tq]})


def init_log():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': 'DEBUG',
            'handlers': ['wsgi']
        }
    })


def start_server():
    app.run(host="0.0.0.0", port=8081, debug=True)


def run():
    init_log()
    load_task()
    start_server()


if __name__ == "__main__":
    run()

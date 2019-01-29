from timer.config import settings
from timer.tasks.core import Manager

from sanic import Sanic
from sanic.response import json

task_manager = Manager()
tasks = task_manager.get_tasks()
app = Sanic(log_config=settings.LOGGING)


@app.route("/")
async def test(request):
    return json({"hello": "world"})


def run():
    app.run(host="0.0.0.0", port=8081, backlog=128)


if __name__ == "__main__":
    run()
